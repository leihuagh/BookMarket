# Generated by Django 2.1.3 on 2018-12-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20181205_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, verbose_name='название'),
        ),
    ]
