# Generated by Django 5.1.6 on 2025-03-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
