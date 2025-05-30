# Generated by Django 5.1.7 on 2025-04-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_radiantpower_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radiantpower',
            options={'ordering': ['name']},
        ),
        migrations.AlterUniqueTogether(
            name='radiantpower',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='radiantpower',
            name='orders',
            field=models.ManyToManyField(related_name='powers', to='api.radiantorder'),
        ),
        migrations.RemoveField(
            model_name='radiantpower',
            name='order',
        ),
    ]
