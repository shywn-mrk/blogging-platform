from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# from blogging_platform.posts.api.permissions import IsBlogUserPermission
from blogging_platform.posts.api.serializers import *
from blogging_platform.posts.filters import PostFilterSet
from blogging_platform.posts.models import *

from .paginations import StandardResultsSetPagination


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsBlogUserPermission]
    permission_classes = [IsAuthenticated]
    filterset_class = PostFilterSet
    pagination_class = StandardResultsSetPagination
    search_fields = ["title"]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)  # type: ignore

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
