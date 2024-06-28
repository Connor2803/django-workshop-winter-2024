# permissions.py
from rest_framework import permissions


# The organizer is the only one allowed to update or delete an post.
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS POST.
        if request.method in [*permissions.SAFE_METHODS, "POST"]:
            return True

        # Write permissions are only allowed to the organiser of the post.
        return obj.author == request.user
