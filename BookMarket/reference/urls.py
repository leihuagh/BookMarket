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

from reference.views import (
    AuthorRefCreateView,
    AuthorRefListView,
    AuthorRefDetailView,
    AuthorRefUpdateView,
    AuthorRefDeleteView,


    GenreRefCreateView,
    GenreRefListView,
    GenreRefDetailView,
    GenreRefUpdateView,
    GenreRefDeleteView,

    SeriesRefCreateView,
    SeriesRefListView,
    SeriesRefDetailView,
    SeriesRefUpdateView,
    SeriesRefDeleteView,

    PublisherRefCreateView,
    PublisherRefListView,
    PublisherRefDetailView,
    PublisherRefUpdateView,
    PublisherRefDeleteView,

    ManufacturerRefCreateView,
    ManufacturerRefListView,
    ManufacturerRefDetailView,
    ManufactorerRefUpdateView,
    ManufactorerRefDeleteView,

    ListReferenceTemplateView,

    OrderStatusRefListView,
    OrderStatusRefCreateView,
    OrderStatusRefUpdateView,
    OrderStatusRefDetailView,
    OrderStatusRefDeleteView,


)

# для иерархии
app_name = 'reference'

urlpatterns = [
    # url авторов
    path('author-ref-create/', AuthorRefCreateView.as_view(), name='author-ref-create'),
    path('author-ref-update/<int:pk>/', AuthorRefUpdateView.as_view(), name='author-ref-update'),
    path('author-ref-detail/<int:pk>/', AuthorRefDetailView.as_view(), name='author-ref-detail'),
    path('author-ref-list/', AuthorRefListView.as_view(), name='author-ref-list'),
    path('author-ref-delete/<int:pk>/', AuthorRefDeleteView.as_view(), name='author-ref-delete'),

    # url жанров
    path('genre-ref-create/', GenreRefCreateView.as_view(), name='genre-ref-create'),
    path('genre-ref-update/<int:pk>/', GenreRefUpdateView.as_view(), name='genre-ref-update'),
    path('genre-ref-detail/<int:pk>/', GenreRefDetailView.as_view(), name='genre-ref-detail'),
    path('genre-ref-list/', GenreRefListView.as_view(), name='genre-ref-list'),
    path('genre-ref-delete/<int:pk>/', GenreRefDeleteView.as_view(), name='genre-ref-delete'),

    # url серий
    path('series-ref-create/', SeriesRefCreateView.as_view(), name='series-ref-create'),
    path('series-ref-update/<int:pk>/', SeriesRefUpdateView.as_view(), name='series-ref-update'),
    path('series-ref-list/', SeriesRefListView.as_view(), name='series-ref-list'),
    path('series-ref-detail/<int:pk>/', SeriesRefDetailView.as_view(), name='series-ref-detail'),
    path('series-ref-delete/<int:pk>/', SeriesRefDeleteView.as_view(), name='series-ref-delete'),

    # url издательств
    path('publisher-ref-create/', PublisherRefCreateView.as_view(), name='publisher-ref-create'),
    path('publisher-ref-update/<int:pk>/', PublisherRefUpdateView.as_view(), name='publisher-ref-update'),
    path('publisher-ref-list/', PublisherRefListView.as_view(), name='publisher-ref-list'),
    path('publisher-ref-detail/<int:pk>/', PublisherRefDetailView.as_view(), name='publisher-ref-detail'),
    path('publisher-ref-delete/<int:pk>/', PublisherRefDeleteView.as_view(), name='publisher-ref-delete'),

    # url изгатовителей
    path('manufacturer-ref-create/', ManufacturerRefCreateView.as_view(), name='manufacturer-ref-create'),
    path('manufacturer-ref-update/<int:pk>/', ManufactorerRefUpdateView.as_view(), name='manufacturer-ref-update'),
    path('manufacturer-ref-list/', ManufacturerRefListView.as_view(), name='manufacturer-ref-list'),
    path('manufacturer-ref-detail/<int:pk>/', ManufacturerRefDetailView.as_view(), name='manufacturer-ref-detail'),
    path('manufacturer-ref-delete/<int:pk>/', ManufactorerRefDeleteView.as_view(), name='manufacturer-ref-delete'),

    path('ref-all-list/', ListReferenceTemplateView.as_view(), name='ref-all-list'),

    path('order-status-ref-list/', OrderStatusRefListView.as_view(), name='order-status-ref-list'),
    path('order-status-ref-create/', OrderStatusRefCreateView.as_view(), name='order-status-ref-create'),
    path('order-status-ref-update/<int:pk>/', OrderStatusRefUpdateView.as_view(), name='order-status-ref-update'),
    path('order-status-ref-detail/<int:pk>/', OrderStatusRefDetailView.as_view(), name='order-status-ref-detail'),
    path('order-status-ref-delete/<int:pk>/', OrderStatusRefDeleteView.as_view(), name='order-status-ref-delete'),
]
