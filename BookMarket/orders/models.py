from django.db import models
from cart.models import Cart
from reference.models import OrderStatus

# Create your models here.


class Orders(models.Model):

    class Meta:
        verbose_name = 'Заказ',
        verbose_name_plural = 'Заказы'

    cart = models.ForeignKey(
        Cart,
        verbose_name='Корзина',
        related_name='cart',
        on_delete=models.PROTECT
    )

    status = models.ForeignKey(
        OrderStatus,
        verbose_name='Статус заказа',
        related_name='status',
        on_delete=models.PROTECT
    )

    phone = models.CharField(
        verbose_name='Телефон для связи',
        help_text='+37529-123-45-67',
        max_length=16
    )

    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='user@mail.com',
        null=True,
        blank=True
    )

    delivery_address = models.TextField(
        verbose_name='Адрес доставки',
        null=True,
        blank=True
    )

    informations = models.TextField(
        verbose_name='Дополнительная информация',
        null=True,
        blank=True
    )

    created_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=False,
        auto_now_add=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Заказ № {}'.format(self.pk)