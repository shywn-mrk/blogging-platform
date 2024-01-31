from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from blogging_platform.posts.api.views import *
from blogging_platform.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()  # type: ignore

router.register("users", UserViewSet)

router.register("posts", PostViewset, basename="post")
router.register("categories", CategoryViewset, basename="category")


app_name = "api"
urlpatterns = router.urls
