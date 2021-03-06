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
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product>/', views.AddProductCartView.as_view(), name='add'),
    path('update/<int:pk>/', views.UpdateProductCartView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteProductCartView.as_view(), name='delete'),
    path('view/', views.ListCartView.as_view(), name='view'),
]