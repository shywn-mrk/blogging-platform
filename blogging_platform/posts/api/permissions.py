from rest_framework.permissions import BasePermission


class IsBlogUserPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.groups.filter(name="blog").exists():
            return True
        return False
