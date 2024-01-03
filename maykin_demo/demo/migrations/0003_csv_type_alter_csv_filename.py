# Generated by Django 4.0.3 on 2024-01-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='type',
            field=models.CharField(default='hello', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='csv',
            name='fileName',
            field=models.FileField(upload_to='csvs'),
        ),
    ]
