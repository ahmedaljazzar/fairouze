from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from accounts.permissions import IsNotAuthenticated
from accounts.serializers import UserSerializer


class AccountsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def create(self, request, *args, **kwargs):
        response = super(AccountsViewSet, self).create(
            request, *args, **kwargs)

        response.data.pop('password')
        return response

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.username != kwargs['username'] \
              and not self.request.user.is_staff:
            raise PermissionDenied()

        response = super(AccountsViewSet, self).retrieve(
            request, *args, **kwargs)

        response.data.pop('password')
        return response

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsNotAuthenticated(), ]

        return [IsAuthenticated(), ]
