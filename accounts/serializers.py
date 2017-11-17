from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from accounts.models import NewsletterSubscription


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    token = serializers.SerializerMethodField()

    def validate_password(self, password):
        """
        Validates the password using the AUTH_PASSWORD_VALIDATORS.

        :param password: The user entered passwod.
        :return: The validated password
        """
        password_validation.validate_password(password, self.instance)
        return password

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )

        # Creating a token for this new user.
        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        try:
            return Token.objects.get(user=obj).key
        except Token.DoesNotExist:
            pass

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'token',
            'date_joined',
            'last_login',
        )


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = ('first_name', 'last_name', 'email',)
