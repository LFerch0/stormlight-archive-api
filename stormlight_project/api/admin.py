from django.contrib import admin
from .models import (
    PoliticalEntity, RadiantOrder, RadiantPower, Book, Chapter, Character, UserFavorite
)

@admin.register(PoliticalEntity)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)

@admin.register(RadiantOrder)
class RadiantOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'spren_type', 'get_powers_count')
    search_fields = ('name', 'description')
    
    def get_powers_count(self, obj):
        return obj.powers.count()
    get_powers_count.short_description = 'Number of Powers'

@admin.register(RadiantPower)
class RadiantPowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_orders')
    search_fields = ('name', 'description')
    filter_horizontal = ('orders',)
    
    def get_orders(self, obj):
        return ", ".join([order.name for order in obj.orders.all()])
    get_orders.short_description = 'Orders'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    search_fields = ('title',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'book')
    search_fields = ('title', 'book__title')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'political_entity')
    search_fields = ('name', 'political_entity__name')
    filter_horizontal = ('radiant_orders',)

@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)