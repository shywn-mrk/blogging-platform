from rest_framework import serializers

from blogging_platform.posts.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        # exclude = ['user']
        read_only_fields = ["user"]
        # depth = 1
