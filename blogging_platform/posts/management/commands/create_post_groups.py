from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from blogging_platform.posts.groups import ALL_GROUPS

User = get_user_model()


class Command(BaseCommand):
    help = "Create all groups related to posts"

    def handle(self, *args, **kwargs):
        for group in ALL_GROUPS:
            Group.objects.get_or_create(name=group)

        self.stdout.write(self.style.SUCCESS("Created groups successfully."))
