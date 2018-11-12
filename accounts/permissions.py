from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    """
    Allows access only to not-authenticated users.
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated()
