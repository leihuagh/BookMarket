from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Author(models.Model):
    # reverse_lazy не работает
    lst_url = 'reference:author-ref-list'

    class Meta:
        verbose_name_plural = 'авторы'
        verbose_name = 'автор'

    name = models.CharField(
        max_length=100,
        verbose_name='автор',
        default=None
    )
    description = models.CharField(
        max_length=200,
        verbose_name='описание автора',
        blank=True,
    )

    def __str__(self):
        return self.name


class Genre(models.Model):

    lst_url = 'reference:genre-ref-list'

    class Meta:
        verbose_name_plural = 'жанры'
        verbose_name = 'жанр'

    name = models.CharField(
        max_length=100,
        verbose_name='жанр'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='описание жанра'
    )

    def __str__(self):
        return self.name


class Series(models.Model):

    lst_url = 'reference:series-ref-list'

    class Meta:
        verbose_name_plural = 'серии'
        verbose_name = 'серия'

    name = models.CharField(
        max_length=100,
        verbose_name='серия'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='описание серии'
    )

    def __str__(self):
        return self.name


class Publisher(models.Model):

    lst_url = 'reference:publisher-ref-list'

    class Meta:
        verbose_name_plural = 'издательства'
        verbose_name = 'издательство'

    name = models.CharField(
        max_length=100,
        verbose_name='издательство'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='описание издательства'
    )

    def __str__(self):
        return self.name


class Manufacturer(models.Model):

    lst_url = 'reference:manufacturer-ref-list'

    class Meta:
        verbose_name_plural = 'изгатовители'
        verbose_name = 'изгатовитель'

    name = models.CharField(
        max_length=100,
        verbose_name='изгатовитель'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='описание изгатовителя'
    )

    def __str__(self):
        return self.name


class OrderStatus(models.Model):

    lst_url = 'reference:order-status-ref-list'

    class Meta:
        verbose_name_plural = 'cтатусы заказов'
        verbose_name = 'cтатус заказа'

    name = models.CharField(
        max_length=100,
        verbose_name='cтатус'
    )

    description = models.CharField(
        max_length=200,
        verbose_name='описание статуса'
    )

    def __str__(self):
        return self.name

