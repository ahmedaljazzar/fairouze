from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    """
    Allows access only to not-authenticated users.
    """
    def has_permission(self, request, view):
        authenticated = request.user and request.user.is_authenticated
        return not authenticated
