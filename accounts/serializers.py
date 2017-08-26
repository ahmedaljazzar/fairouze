from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

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
            validated_data['password']
        )

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
