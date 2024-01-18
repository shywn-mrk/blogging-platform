from rest_framework import viewsets

from blogging_platform.posts.api.serializers import *
from blogging_platform.posts.filters import PostFilterSet
from blogging_platform.posts.models import *

from .paginations import StandardResultsSetPagination


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilterSet
    pagination_class = StandardResultsSetPagination


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
