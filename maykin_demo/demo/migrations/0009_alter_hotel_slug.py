# Generated by Django 4.0.3 on 2024-01-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_alter_hotel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]