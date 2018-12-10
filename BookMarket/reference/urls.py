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

from reference.views import AuthorRefCreateView, GenreRefCreateView, SeriesRefCreateView, \
    PublisherRefCreateView, ManufacturerRefCreateView, AuthorRefUpdateView, GenreRefUpdateView, \
    SeriesRefUpdateView, PublisherRefUpdateView, ManufactorerRefUpdateView, DetailAuthorRefView, DetailGenreRefView, ListAuthorRefView

urlpatterns = [
    path('admin-shop/ref/author-ref-create/', AuthorRefCreateView.as_view()),
    path('admin-shop/ref/genre-ref-create/', GenreRefCreateView.as_view()),
    path('admin-shop/ref/series-ref-create/', SeriesRefCreateView.as_view()),
    path('admin-shop/ref/publisher-ref-create/', PublisherRefCreateView.as_view()),
    path('admin-shop/ref/manufacturer-ref-create/', ManufacturerRefCreateView.as_view()),
    path('admin-shop/ref/author-ref-update/<int:pk>/', AuthorRefUpdateView.as_view()),
    path('admin-shop/ref/genre-ref-update/<int:pk>/', GenreRefUpdateView.as_view()),
    path('admin-shop/ref/series-ref-update/<int:pk>/', SeriesRefUpdateView.as_view()),
    path('admin-shop/ref/publisher-ref-update/<int:pk>/', PublisherRefUpdateView.as_view()),
    path('admin-shop/ref/manufactorer-ref-update/<int:pk>/', ManufactorerRefUpdateView.as_view()),
    path('admin-shop/ref/author-ref-detail/<int:pk>/', DetailAuthorRefView.as_view()),
    path('admin-shop/ref/genre-ref-detail/<int:pk>/', DetailGenreRefView.as_view()),

    path('admin-shop/ref/author-ref-list/', ListAuthorRefView.as_view())
]
