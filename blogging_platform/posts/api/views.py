from rest_framework import viewsets

from blogging_platform.posts.api.serializers import *
from blogging_platform.posts.filters import PostFilterSet
from blogging_platform.posts.models import *

from .paginations import StandardResultsSetPagination

# from blogging_platform.posts.api.permissions import IsBlogUserPermission


class PostViewset(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsBlogUserPermission]
    filterset_class = PostFilterSet
    pagination_class = StandardResultsSetPagination
    search_fields = ["title"]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)  # type: ignore

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
