from django.contrib import admin
from reference.models import Author, Genre, Series, Publisher, Manufacturer, OrderStatus

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Publisher)
admin.site.register(Manufacturer)
admin.site.register(OrderStatus)
