from django.db import models

# Create your models here.


class Author(models.Model):

    class Meta:
        verbose_name_plural = 'Authors'

    name = models.CharField(
        max_length=50,
        verbose_name='автор'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='об авторе'
    )


class Genre(models.Model):

    class Meta:
        verbose_name_plural = 'Genres'

    name = models.CharField(
        max_length=50,
        verbose_name='жанр'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='о жанре'
    )


class Series(models.Model):

    class Meta:
        verbose_name_plural = 'Series'

    name = models.CharField(
        max_length=50,
        verbose_name='серия'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='о серии'
    )


class Publisher(models.Model):

    class Meta:
        verbose_name_plural = 'Publishers'

    name = models.CharField(
        max_length=50,
        verbose_name='издательство'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='об издательстве'
    )


class Manufacturer(models.Model):

    class Meta:
        verbose_name_plural = 'Manufacturers'

    name = models.CharField(
        max_length=50,
        verbose_name='изгатовитель'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='об изгатовителе'
    )

