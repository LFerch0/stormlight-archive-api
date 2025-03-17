# Generated by Django 5.1.7 on 2025-03-12 20:25

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, unique=True)),
                ('publication_date', models.DateField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('description', models.TextField()),
                ('total_pages', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('parts', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('chapters_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['publication_date'],
            },
        ),
        migrations.CreateModel(
            name='RadiantOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('spren_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('first_ideal', models.TextField(default='Life before death. Strength before weakness. Journey before destination.')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='api_nation_name_0bea37_idx')],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField()),
                ('dahn_nahn', models.CharField(max_length=50)),
                ('nation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houses', to='api.nation')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('aliases', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='characters/')),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='api.house')),
                ('nation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='citizens', to='api.nation')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CharacterRadiantOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_ideal', models.PositiveSmallIntegerField(choices=[(1, 'First Ideal'), (2, 'Second Ideal'), (3, 'Third Ideal'), (4, 'Fourth Ideal'), (5, 'Fifth Ideal')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('has_blade', models.BooleanField(default=False)),
                ('has_plate', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.radiantorder')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='radiant_orders',
            field=models.ManyToManyField(blank=True, through='api.CharacterRadiantOrder', to='api.radiantorder'),
        ),
        migrations.CreateModel(
            name='RadiantPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radiant_powers', to='api.radiantorder')),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(blank=True, related_name='favorited_by', to='api.book')),
                ('characters', models.ManyToManyField(blank=True, related_name='favorited_by', to='api.character')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.PositiveIntegerField()),
                ('pages', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='api.book')),
                ('pov_character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pov_chapters', to='api.character')),
            ],
            options={
                'ordering': ['book', 'number'],
                'indexes': [models.Index(fields=['book', 'number'], name='api_chapter_book_id_4881fd_idx')],
                'unique_together': {('book', 'number')},
            },
        ),
        migrations.AddIndex(
            model_name='house',
            index=models.Index(fields=['name'], name='api_house_name_54b4db_idx'),
        ),
        migrations.AddIndex(
            model_name='house',
            index=models.Index(fields=['nation'], name='api_house_nation__dec301_idx'),
        ),
        migrations.AddIndex(
            model_name='characterradiantorder',
            index=models.Index(fields=['character', 'order'], name='api_charact_charact_d64fae_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='characterradiantorder',
            unique_together={('character', 'order')},
        ),
        migrations.AddIndex(
            model_name='character',
            index=models.Index(fields=['name'], name='api_charact_name_b23034_idx'),
        ),
        migrations.AddIndex(
            model_name='character',
            index=models.Index(fields=['house'], name='api_charact_house_i_500e52_idx'),
        ),
        migrations.AddIndex(
            model_name='character',
            index=models.Index(fields=['nation'], name='api_charact_nation__6b9d75_idx'),
        ),
        migrations.AddIndex(
            model_name='radiantpower',
            index=models.Index(fields=['name'], name='api_radiant_name_b816c8_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='radiantpower',
            unique_together={('name', 'order')},
        ),
        migrations.AddIndex(
            model_name='userfavorite',
            index=models.Index(fields=['user'], name='api_userfav_user_id_eb2395_idx'),
        ),
    ]
