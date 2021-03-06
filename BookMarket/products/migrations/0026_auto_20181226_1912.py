# Generated by Django 2.1.3 on 2018-12-26 16:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20181213_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateField(blank=True, default=datetime.date(2018, 12, 26), null=True, verbose_name='дата внесения в каталог'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='reference.Series', verbose_name='серия'),
        ),
    ]
