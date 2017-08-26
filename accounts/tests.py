from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts import views, factories
from accounts.permissions import IsNotAuthenticated


class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user.
        self.pre_data = {
            'username': 'pre_user',
            'email': 'pre_user@example.com',
            'password': 'pre_user_password',
        }
        self.test_user = factories.UserFactory.create(**self.pre_data)

        # URL for creating an account.
        self.url = reverse('register')

        # Be more adaptive to changes
        self.set_test_authentication()

    def set_test_authentication(self):
        """
        This method is used to reduce the code fragility. Just in
        case we want to allow authenticated users to create a new
        user, the test suit must adapt to this change.

        This must be Ok since we are checking for view permissions in
        `test_authenticated_user_register` test.
        """
        view_permissions = views.RegisterAPIView.permission_classes
        if IsNotAuthenticated in view_permissions:
            self.client.force_authenticate(user=None)
        else:
            self.client.force_authenticate(user=self.test_user)

    def test_create_user_successful(self):
        """
        Ensure we can create a new user and a valid token is created
        with it.
        """
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'test_password'
        }
        resp = self.client.post(self.url, data, format='json')

        # We want to make sure we get 201 created code,
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # And that we have two users in the database.
        self.assertEqual(User.objects.count(), 2)

        # Additionally, we want to return the username and email upon
        # successful creation, but not the password!
        self.assertEqual(resp.data['username'], data['username'])
        self.assertEqual(resp.data['email'], data['email'])
        self.assertFalse('password' in resp.data)
        self.assertFalse(data['password'] in resp.data)

        # Ensure we created and included the Token upon successful
        # registration of a user
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEqual(resp.data['token'], token.key)

    def test_authenticated_user_register(self):
        user = User.objects.get(username=self.pre_data['username'])
        self.client.force_authenticate(user=user)
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'test_password'
        }
        resp = self.client.post(self.url, data, format='json')

        # Make an authenticated request to the view...
        self.assertTrue(user.is_authenticated)

        # The authenticated user isn't allowed to perform this action
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_with_short_password(self):
        """
        Ensure user is not created for password lengths less than 8.
        """
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': 'foo'
        }

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['password']), 1)

    def test_create_user_with_no_password(self):
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': ''
        }

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['password']), 1)

    def test_create_user_with_too_long_username(self):
        data = {
            'username': 'foo'*30,
            'email': 'foobarbaz@example.com',
            'password': 'foobar'
        }

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['username']), 1)

    def test_create_user_with_no_username(self):
        data = {
            'username': '',
            'email': 'foobarbaz@example.com',
            'password': 'foobar'
        }

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['username']), 1)

    def test_create_user_with_preexisting_username(self):
        data = self.pre_data.copy()
        data['email'] = 'new_username@example.com'

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['username']), 1)

    def test_create_user_with_preexisting_email(self):
        data = self.pre_data.copy()
        data['username'] = 'new_username'

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['email']), 1)

    def test_create_user_with_invalid_email(self):
        data = {
            'username': 'foobarbaz',
            'email':  'testing',
            'password': 'foobarbaz'
        }

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['email']), 1)

    def test_create_user_with_no_email(self):
        data = {
            'username': 'foobar',
            'email': '',
            'password': 'foobarbaz'
        }

        resp = self.client.post(self.url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(resp.data['email']), 1)
