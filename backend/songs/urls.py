from django.urls import include, path
from rest_framework import routers
from songs.views import SongViewSet

router = routers.DefaultRouter()
router.register(r"song", SongViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
