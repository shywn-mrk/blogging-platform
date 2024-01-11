from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from blogging_platform.users.api.views import UserViewSet
from posts.api.views import *

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register("posts", PostViewset)
router.register("categories", CategoryViewset)


app_name = "api"
urlpatterns = router.urls
