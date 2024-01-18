import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError
from django.utils.crypto import get_random_string

from blogging_platform.posts.models import Category, Post

User = get_user_model()


class Command(BaseCommand):
    help = "Populate the database with 10000 posts and 40 categories"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        categories = [Category(name=f"Category {i}") for i in range(1, 41)]
        Category.objects.bulk_create(categories)

        users = [User(email=f"user{i}@example.com") for i in range(1, 101)]
        User.objects.bulk_create(users)

        for i in range(1, 10001):
            try:
                Post.objects.create(
                    title=f"Post {i}",
                    body=get_random_string(400),
                    category=random.choice(categories),
                    user=random.choice(users),
                    is_published=random.choice([True, False]),
                )
            except IntegrityError:
                self.stdout.write(self.style.ERROR("Database populated failed."))

        self.stdout.write(self.style.SUCCESS("Database populated successfully."))
