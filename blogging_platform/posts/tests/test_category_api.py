from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from blogging_platform.posts.models import Category

User = get_user_model()


class CategoryViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@gmail.com", password="12345"
        )
        self.client.login(username="testuser@gmail.com", password="12345")
        # This is correct
        self.category = Category.objects.create(name="Test Category")
        # This is wrong
        # self.client.post('/api/categories/', {"name": "Test Category"})

    def test_list_categories(self):
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_category(self):
        response = self.client.post(
            "/api/categories/", {"name": "New Category"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Category.objects.filter(name="New Category").exists())
