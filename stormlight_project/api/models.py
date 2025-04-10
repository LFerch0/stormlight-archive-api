from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

class PoliticalEntity(models.Model):
    ENTITY_TYPES = [
        ('nation', 'Nation'),
        ('unclaimed_land', 'Unclaimed Land'),
        ('city', 'City'),
        ('city_state', 'City State'),
        ('ocean', 'Ocean'),
        ('continent', 'Continent'),
        ('region', 'Region'),
        ('village', 'Village'),
        ('fortress', 'Fortress'),
        ('island', 'Island'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, db_index=True)
    entity_type = models.CharField(
        max_length=20,
        choices=ENTITY_TYPES,
        default='other',
        db_index=True
    )
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['entity_type']),
        ]

    def __str__(self):
        return self.name
    
class RadiantOrder(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    spren_type = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class RadiantPower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    orders = models.ManyToManyField(RadiantOrder, related_name='powers')
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        order_names = ", ".join([order.name for order in self.orders.all()])
        return f"{self.name} ({order_names})"

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True)
    total_pages = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    chapters_count = models.PositiveIntegerField(default=0)
    total_words = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])
    publication_date = models.DateField()
    notes = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True, blank=True, related_name='books_as_flashback')

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    part = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        ordering = ['book', 'number']
        indexes = [
            models.Index(fields=['book', 'number']),
        ]
    
    def __str__(self):
        if self.number:
            return f"{self.book.title} - Chapter {self.number}: {self.title or 'Untitled'}"
        else:
            return f"{self.book.title} - {self.title or 'Untitled'}"

class Character(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    aliases = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    political_entity = models.CharField(max_length=200, blank=True, null=True)
    radiant_orders = models.ManyToManyField(RadiantOrder, blank=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['political_entity']),
        ]

    def __str__(self):
        return self.name

class UserFavorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='favorites')
    characters = models.ManyToManyField(Character, blank=True, related_name='favorited_by')
    books = models.ManyToManyField(Book, blank=True, related_name='favorited_by')

    class Meta:
        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"{self.user.username}'s favorites"