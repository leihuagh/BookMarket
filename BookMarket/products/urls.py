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
from products.views import BookProdListView, BookProdCreateView, BookProdDetailView, BookProdUpdateView, BookProdDeleteView

app_name = 'products'

urlpatterns = [
    # url авторов
    path('book-prod-list/', BookProdListView.as_view(), name='book-prod-list'),
    path('book-prod-create/', BookProdCreateView.as_view(), name='book-prod-create'),
    path('book-prod-view/<int:pk>/', BookProdDetailView.as_view(), name='book-prod-view'),
    path('book-prod-update/<int:pk>/', BookProdUpdateView.as_view(), name='book-prod-update'),
    path('book-prod-delete/<int:pk>/', BookProdDeleteView.as_view(), name='book-prod-delete'),
]