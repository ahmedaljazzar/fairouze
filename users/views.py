from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users.permissions import IsNotAuthenticated
from users.serializers import UserSerializer


class RegisterAPIView(generics.CreateAPIView):
    """
    **Use Cases**

        Basically, creates a new user.

    **Example Requests**

        POST /api/register

    **Request Body**

        The request body should be a "application/json" encoded object,
        containing the following items:

        username
            A uniques username for the new user.
        email
            A uniques email for the new user.
        password
            No less than 8 characters.

    **Response Values**

        If the user is logged in, an HTTP 403 "Forbidden" response
        is returned.

        If the user is not logged in and the provided data is not
        valid, an HTTP 400 "Bad Request" response is returned with
        a json list of the error messages.

        Otherwise, an HTTP 201 "Created" response is returned. The
        response contains the following value:

        username:
            The username associated with the created account.
        email:
            The email associated with the created account.
        token:
            The token generated specifically for the created account.

    **Example Response**

            {
                "username": "newuser",
                "email": "newuser@example.com",
                "token": "notTopS3cre7",
            }

    """
    permission_classes = (IsNotAuthenticated,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Will accept a request from an unauthenticated user that
        contains an email, a password, and a username and will create
        a new account and an auth token for the user.

        :param request:
        :param args:
        :param kwargs:
        :return: - HTTP_201_CREATED if the account created successfully.
                 - HTTP_403_FORBIDDEN if the user is authenticated.
                 - HTTP_400_BAD_REQUEST if the user passed non-sense
                   data.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Creating a token for this new user.
            token = Token.objects.create(user=user)
            user_data = {
                'username': serializer.data['username'],
                'email': serializer.data['email'],
                'token': token.key,
            }

            return Response(user_data, status=status.HTTP_201_CREATED)

        # Inform the user about the mistakes he made.
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)