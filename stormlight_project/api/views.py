from django.shortcuts import render


from rest_framework import viewsets
from .models import (
    PoliticalEntity, RadiantOrder, RadiantPower, Book, Chapter, Character, UserFavorite
)
from .serializers import (
    PoliticalEntitySerializer, RadiantOrderSerializer, RadiantPowerSerializer, BookSerializer, ChapterSerializer, CharacterSerializer, UserFavoriteSerializer
)

class NationViewSet(viewsets.ModelViewSet):
    queryset = PoliticalEntity.objects.all()
    serializer_class = PoliticalEntitySerializer

class RadiantOrderViewSet(viewsets.ModelViewSet):
    queryset = RadiantOrder.objects.all()
    serializer_class = RadiantOrderSerializer

class RadiantPowerViewSet(viewsets.ModelViewSet):
    queryset = RadiantPower.objects.all()
    serializer_class = RadiantPowerSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer  


class UserFavoriteViewSet(viewsets.ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer