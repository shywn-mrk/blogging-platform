from rest_framework.permissions import BasePermission

from blogging_platform.posts.groups import BLOG


class IsBlogUserPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.groups.filter(name=BLOG).exists():
            return True
        return False
