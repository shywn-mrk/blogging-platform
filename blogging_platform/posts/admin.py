from django.contrib import admin

from blogging_platform.posts.models import *

admin.site.register(Category)
admin.site.register(Post)
