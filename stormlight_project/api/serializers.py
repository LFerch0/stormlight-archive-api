from rest_framework import serializers
from .models import (
    Nation, RadiantOrder, RadiantPower, Book, Chapter,
    House, Character, CharacterRadiantOrder, UserFavorite
)

class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = '__all__'

class RadiantOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiantOrder
        fields = '__all__'

class RadiantPowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiantPower
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class CharacterRadiantOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterRadiantOrder
        fields = '__all__'

class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = '__all__'