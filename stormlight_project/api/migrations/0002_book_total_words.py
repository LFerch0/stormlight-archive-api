# Generated by Django 5.1.7 on 2025-03-14 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_words',
            field=models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
