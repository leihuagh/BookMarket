"""Market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.views import HomeTemplateView, AboutTemplateView, DeliveryTemplateView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-shop/', include('admincore.urls')),
    path('reference/', include('reference.urls')),
    path('products/', include('products.urls')),
    path('', HomeTemplateView.as_view(), name='Core'),
    path('about', AboutTemplateView.as_view(), name='About'),
    path('delivery', DeliveryTemplateView.as_view(), name='Delivery'),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
