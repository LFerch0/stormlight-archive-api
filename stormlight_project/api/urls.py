from django.urls import path, include
from rest_framework import routers
from .views import (
    NationViewSet, RadiantOrderViewSet, RadiantPowerViewSet,
    BookViewSet, ChapterViewSet,
    CharacterViewSet,
    UserFavoriteViewSet
)

router = routers.DefaultRouter()
router.register(r'locations', NationViewSet)
router.register(r'radiant-orders', RadiantOrderViewSet)
router.register(r'radiant-powers', RadiantPowerViewSet)
router.register(r'books', BookViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'user-favorites', UserFavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
