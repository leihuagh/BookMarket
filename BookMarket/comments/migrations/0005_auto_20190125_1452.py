# Generated by Django 2.1.3 on 2019-01-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_comments_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]