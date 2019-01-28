from django.db import models
from reference.models import Author, Series, Genre, Publisher, Manufacturer
import datetime

# Create your models here.


class Book(models.Model):

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'

    name = models.CharField(
        max_length=50,
        verbose_name='название'
    )

    cover_image = models.ImageField(
        verbose_name='обложка',
        default=None,
        blank=True
    )

    price = models.DecimalField(
        decimal_places=0,
        max_digits=5,
        verbose_name='стоимость',
        default=0.0
    )

    authors = models.ManyToManyField(
        Author,
        verbose_name='автор'
    )

    series = models.ForeignKey(
        Series,
        verbose_name='серия',
        on_delete=models.CASCADE,
        default=None,
        related_name='books'
    )

    genre = models.ManyToManyField(
        Genre,
        verbose_name='жанр'
    )

    date_of_published = models.CharField(
        max_length=4,
        verbose_name='год издания',
        default=None,
        blank=True,
        null=True
    )

    numbers_of_pages = models.PositiveIntegerField(
        verbose_name='количество страниц',
        default=None
    )

    binding = models.CharField(
        max_length=50,
        verbose_name='переплет',
        default=None
    )

    pr_format = models.CharField(
        max_length=50,
        verbose_name='формат',
        default=None
    )

    isbn = models.CharField(
        max_length=50,
        verbose_name='ISBN',
        default=None
    )

    weight = models.PositiveIntegerField(
        verbose_name='вес, гр.',
        default=None
    )

    age_limit = models.CharField(
        max_length=10,
        verbose_name='возрастные ограничения',
        default=None
    )

    publisher = models.ForeignKey(
        Publisher,
        verbose_name='издательство',
        on_delete=models.CASCADE,
        default=None
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name='изготовитель',
        on_delete=models.CASCADE,
        default=None
    )

    stock = models.PositiveIntegerField(
        verbose_name='в наличии',
        default=None
    )

    available = models.BooleanField(
        verbose_name='доступен',
        default=False
    )

    rating = models.SmallIntegerField(
        verbose_name='рейтинг (0 - 10)',
        default=None
    )

    created = models.DateField(
        verbose_name='дата внесения в каталог',
        default=datetime.date.today(),
        blank=True,
        null=True
    )

    updated = models.DateField(
        verbose_name='дата последнего изменения карточки',
        default=None,
        blank=True,
        null=True
    )

    def get_field(self):
        flds = dict((field.verbose_name, field.value_to_string(self)) for field in self._meta.fields)
        flds.pop('ID', None)
        flds.pop('название', None)
        flds.pop('обложка', None)
        return flds

    def __str__(self):
        return self.name



