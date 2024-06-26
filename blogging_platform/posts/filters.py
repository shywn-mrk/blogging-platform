from django_filters import rest_framework as filters

from .models import Post


class PostFilterSet(filters.FilterSet):
    class Meta:
        model = Post
        fields = ["category", "created_at"]
