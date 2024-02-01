from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase

from blogging_platform.posts.groups import BLOG
from blogging_platform.posts.models import Category, Post

User = get_user_model()


class PostViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@gmail.com", password="12345"
        )
        self.blog_group = Group.objects.create(name=BLOG)
        self.client.login(username="testuser@gmail.com", password="12345")
        self.category = Category.objects.create(name="Test Category")
        self.post_data = {
            "title": "Test Post",
            "body": "This is a test post content.",
            "category": self.category.pk,
        }

    def test_create_post(self):
        response = self.client.post("/api/posts/", self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Post.objects.filter(title="Test Post").exists())

    def test_list_posts(self):
        Post.objects.create(
            title="Post 1",
            body="Content 1",
            user=self.user,
            category=self.category,
        )
        Post.objects.create(
            title="Post 2",
            body="Content 2",
            user=self.user,
            category=self.category,
        )
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(len(response.data["results"]), 2)
