from django.contrib import admin
from .models import (
    Nation, RadiantOrder, RadiantPower, Book, Chapter,
    House, Character, CharacterRadiantOrder, UserFavorite
)

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location')
    search_fields = ('name',)

@admin.register(RadiantOrder)
class RadiantOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'spren_type')
    search_fields = ('name',)

@admin.register(RadiantPower)
class RadiantPowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'order__name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    search_fields = ('title',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'book')
    search_fields = ('title', 'book__title')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'nation', 'dahn_nahn')
    search_fields = ('name', 'nation__name')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'house', 'nation')
    search_fields = ('name', 'house__name', 'nation__name')

@admin.register(CharacterRadiantOrder)
class CharacterRadiantOrderAdmin(admin.ModelAdmin):
    list_display = ('character', 'order', 'current_ideal')
    search_fields = ('character__name', 'order__name')

@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)