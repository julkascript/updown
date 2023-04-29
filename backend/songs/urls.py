from django.urls import include, path
from rest_framework import routers
from songs.views import ArtistViewSet, SongViewSet

router = routers.DefaultRouter()
router.register(r"song", SongViewSet)
router.register(r"artist", ArtistViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
