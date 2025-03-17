from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

class Nation(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return self.name

class RadiantOrder(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    spren_type = models.CharField(max_length=100)
    description = models.TextField()
    first_ideal = models.TextField(default="Life before death. Strength before weakness. Journey before destination.")
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class RadiantPower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.ForeignKey(RadiantOrder, on_delete=models.CASCADE, related_name='radiant_powers')
    
    class Meta:
        ordering = ['order', 'name']
        unique_together = ['name', 'order']
        indexes = [
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.order.name})"

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    description = models.TextField()
    total_pages = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    total_words = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])
    parts = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    chapters_count = models.PositiveIntegerField(default=0)
    main_flashback_character = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True, blank=True, related_name='books_as_flashback')
    
    class Meta:
        ordering = ['publication_date']
    
    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    number = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    pages = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    pov_character = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True, blank=True, related_name='pov_chapters')
    
    class Meta:
        ordering = ['book', 'number']
        unique_together = ['book', 'number']
        indexes = [
            models.Index(fields=['book', 'number']),
        ]
    
    def __str__(self):
        return f"{self.book.title} - Chapter {self.number}: {self.title or 'Untitled'}"

class House(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    nation = models.ForeignKey(Nation, on_delete=models.SET_NULL, null=True, related_name='houses')
    dahn_nahn = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['nation']),
        ]
    
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    aliases = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    description = models.TextField()
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    nation = models.ForeignKey(Nation, on_delete=models.SET_NULL, null=True, blank=True, related_name='citizens')
    radiant_orders = models.ManyToManyField(RadiantOrder, through='CharacterRadiantOrder', blank=True)
    image = models.ImageField(upload_to='characters/', blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['house']),
            models.Index(fields=['nation']),
        ]
    
    def __str__(self):
        return self.name

class CharacterRadiantOrder(models.Model):
    IDEAL_CHOICES = [
        (1, 'First Ideal'),
        (2, 'Second Ideal'),
        (3, 'Third Ideal'),
        (4, 'Fourth Ideal'),
        (5, 'Fifth Ideal'),
    ]
    
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    order = models.ForeignKey(RadiantOrder, on_delete=models.CASCADE)
    current_ideal = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=IDEAL_CHOICES
    )
    has_blade = models.BooleanField(default=False)
    has_plate = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('character', 'order')
        indexes = [
            models.Index(fields=['character', 'order']),
        ]
    
    def __str__(self):
        return f"{self.character.name} - {self.order.name} ({self.get_current_ideal_display()})"

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