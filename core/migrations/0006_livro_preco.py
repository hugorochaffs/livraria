# Generated by Django 5.2 on 2025-04-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_autor_options_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='preco',
            field=models.FloatField(null=True),
        ),
    ]
