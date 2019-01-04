from django.contrib import admin

from . import models


# Register your models here.

class CartAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'created_date',
        'updated_date'
    ]

    class Meta:
        model = models.Cart


class ProductsInCartAdmin(admin.ModelAdmin):

    list_display = [
        'cart',
        'book',
        'quantity'
    ]

    class Meta:
        model = models.ProductsInCart


admin.site.register(models.ProductsInCart, ProductsInCartAdmin)
admin.site.register(models.Cart, CartAdmin)
