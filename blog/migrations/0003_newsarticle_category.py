# Generated by Django 5.1.1 on 2024-10-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_newsarticle_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='category',
            field=models.CharField(blank=True, choices=[('sports', 'Sports'), ('Agriculture', 'Agriculture'), ('technology', 'Technology'), ('health', 'Health')], default='', max_length=50, null=True),
        ),
    ]
