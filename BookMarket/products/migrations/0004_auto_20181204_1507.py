# Generated by Django 2.1.3 on 2018-12-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=5, verbose_name='стоимость'),
        ),
    ]