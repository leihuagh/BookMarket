from django.db import models
from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from .signals import profile_creator

User = get_user_model()


class Prf(models.Model):

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'

    customer = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )

    delivery_address = models.TextField(
        'Адрес доставки',
        default='Заполнить'
    )

    def __str__(self):
        return self.delivery_address

# post_save.connect(profile_creator, sender=User)
