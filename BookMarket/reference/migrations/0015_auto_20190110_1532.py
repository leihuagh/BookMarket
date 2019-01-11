# Generated by Django 2.1.3 on 2019-01-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0014_auto_20181205_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Статус')),
                ('description', models.CharField(max_length=200, verbose_name='описание статуса')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказов',
            },
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'изгатовитель', 'verbose_name_plural': 'изгатовители'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'издательство', 'verbose_name_plural': 'издательства'},
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='описание автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default=None, max_length=100, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.CharField(max_length=200, verbose_name='описание жанра'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='description',
            field=models.CharField(max_length=200, verbose_name='описание изгатовителя'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='изгатовитель'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='description',
            field=models.CharField(max_length=200, verbose_name='описание издательства'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100, verbose_name='издательство'),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.CharField(max_length=200, verbose_name='описание серии'),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=100, verbose_name='серия'),
        ),
    ]
