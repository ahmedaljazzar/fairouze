from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import IsNotAuthenticated
from users.serializers import UserSerializer


class RegisterAPIView(APIView):
    """
    Basically, creates the user.
    """
    permission_classes = [IsNotAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)

            user_data = serializer.data.copy()
            user_data.pop('password')
            user_data['token'] = token.key

            return Response(user_data, status=status.HTTP_201_CREATED)

        raise ValidationError(detail=serializer.errors)