# Generated by Django 2.1.3 on 2019-02-11 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190211_2354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'permissions': (('can_view_order_custom', 'Can view order custom'),), 'verbose_name': ('Заказ',), 'verbose_name_plural': 'Заказы'},
        ),
    ]
