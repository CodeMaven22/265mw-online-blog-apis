# Generated by Django 5.1.1 on 2024-10-14 10:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_newsarticle_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
