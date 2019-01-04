from django.db import models
from django.contrib.auth import get_user_model
from products.models import Book
# Create your models here.


User = get_user_model()


class Cart(models.Model):

    user = models.ForeignKey(
        User,
        related_name='carts',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    created_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False,
        auto_now_add=True
    )

    updated_date = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return 'Корзина №{} для пользователя {}'.format(
            self.pk,
            self.user
        )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class ProductsInCart(models.Model):

    cart = models.ForeignKey(
        Cart,
        related_name='products',
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        related_name='product_in_cart',
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        'Количество',
        default=1,
    )

    def __str__(self):
        return 'Книга {name} в корзине {cart_id}'.format(
            name=self.book.name,
            cart_id=self.cart.pk
        )

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
        unique_together = (
            ('cart', 'book'),
        )
