# Generated by Django 5.1.4 on 2025-04-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='nome',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
