from django.shortcuts import render


from rest_framework import viewsets
from .models import (
    Nation, RadiantOrder, RadiantPower, Book, Chapter,
    House, Character, CharacterRadiantOrder, UserFavorite
)
from .serializers import (
    NationSerializer, RadiantOrderSerializer, RadiantPowerSerializer,
    BookSerializer, ChapterSerializer, HouseSerializer,
    CharacterSerializer, CharacterRadiantOrderSerializer,
    UserFavoriteSerializer
)

class NationViewSet(viewsets.ModelViewSet):
    queryset = Nation.objects.all()
    serializer_class = NationSerializer

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

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterRadiantOrderViewSet(viewsets.ModelViewSet):
    queryset = CharacterRadiantOrder.objects.all()
    serializer_class = CharacterRadiantOrderSerializer

class UserFavoriteViewSet(viewsets.ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer