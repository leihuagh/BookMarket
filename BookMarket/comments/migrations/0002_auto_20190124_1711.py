# Generated by Django 2.1.3 on 2019-01-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='tag',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments',
            field=models.SlugField(default=None, verbose_name='Comments'),
        ),
    ]
