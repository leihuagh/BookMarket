from django.db import models

# Create your models here.


class Author(models.Model):

    class Meta:
        verbose_name_plural = 'авторы'
        verbose_name = 'автор'

    name = models.CharField(
        max_length=50,
        verbose_name='автор',
        default=None
    )
    description = models.CharField(
        max_length=200,
        verbose_name='об авторе',
        blank=True,
    )

    def get_update_url(self):
        return '/shopadmin/admin-shop/ref/author-ref-update/{}/'.format(self.pk)

    def get_view_url(self):
        return '/shopadmin/admin-shop/ref/author-ref-detail/{}/'.format(self.pk)

    def __str__(self):
        return self.name


class Genre(models.Model):

    class Meta:
        verbose_name_plural = 'жанры'
        verbose_name = 'жанр'

    name = models.CharField(
        max_length=50,
        verbose_name='жанр'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='о жанре'
    )

    def __str__(self):
        return self.name


class Series(models.Model):

    class Meta:
        verbose_name_plural = 'серии'
        verbose_name = 'серия'

    name = models.CharField(
        max_length=50,
        verbose_name='серия'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='о серии'
    )

    def __str__(self):
        return self.name


class Publisher(models.Model):

    class Meta:
        verbose_name_plural = 'Издательства'
        verbose_name = 'Издательство'

    name = models.CharField(
        max_length=50,
        verbose_name='издательство'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='об издательстве'
    )

    def __str__(self):
        return self.name


class Manufacturer(models.Model):

    class Meta:
        verbose_name_plural = 'Изгатовители'
        verbose_name = 'Изгатовитель'

    name = models.CharField(
        max_length=50,
        verbose_name='изгатовитель'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='об изгатовителе'
    )

    def __str__(self):
        return self.name



