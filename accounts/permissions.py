from rest_framework.compat import is_authenticated
from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    """
    Allows access only to not-authenticated users.
    """
    def has_permission(self, request, view):
        return not is_authenticated(request.user)
