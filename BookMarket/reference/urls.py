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
    SeriesRefUpdateView, PublisherRefUpdateView, ManufactorerRefUpdateView, AuthorRefDetailView, GenreRefDetailView, \
    AuthorRefListView, AuthorRefDeleteView, GenreRefListView, GenreRefDeleteView, SeriesRefListView, \
    SeriesRefDetailView, SeriesRefDeleteView, PublisherRefListView, PublisherRefDetailView, PublisherRefDeleteView, \
    ManufacturerRefListView, ManufacturerRefDetailView, ManufactorerRefDeleteView

urlpatterns = [
    path('ref/author-ref-create/', AuthorRefCreateView.as_view()),
    path('ref/author-ref-update/<int:pk>/', AuthorRefUpdateView.as_view()),
    path('ref/author-ref-detail/<int:pk>/', AuthorRefDetailView.as_view()),
    path('ref/author-ref-list/', AuthorRefListView.as_view(), name='AuthorRefeList'),
    path('ref/author-ref-delete/<int:pk>/', AuthorRefDeleteView.as_view()),

    path('ref/genre-ref-create/', GenreRefCreateView.as_view()),
    path('ref/genre-ref-update/<int:pk>/', GenreRefUpdateView.as_view()),
    path('ref/genre-ref-detail/<int:pk>/', GenreRefDetailView.as_view()),
    path('ref/genre-ref-list/', GenreRefListView.as_view(), name='GenreRefList'),
    path('ref/genre-ref-delete/<int:pk>/', GenreRefDeleteView.as_view()),

    path('ref/series-ref-create/', SeriesRefCreateView.as_view()),
    path('ref/series-ref-update/<int:pk>/', SeriesRefUpdateView.as_view()),
    path('ref/series-ref-list/', SeriesRefListView.as_view(), name='SeriesRefList'),
    path('ref/series-ref-detail/<int:pk>/', SeriesRefDetailView.as_view()),
    path('ref/series-ref-delete/<int:pk>/', SeriesRefDeleteView.as_view()),

    path('ref/publisher-ref-create/', PublisherRefCreateView.as_view()),
    path('ref/publisher-ref-update/<int:pk>/', PublisherRefUpdateView.as_view()),
    path('ref/publisher-ref-list/', PublisherRefListView.as_view(), name='PublisherRefList'),
    path('ref/publisher-ref-detail/<int:pk>/', PublisherRefDetailView.as_view()),
    path('ref/publisher-ref-delete/<int:pk>/', PublisherRefDeleteView.as_view()),

    path('ref/manufacturer-ref-create/', ManufacturerRefCreateView.as_view()),
    path('ref/manufacturer-ref-update/<int:pk>/', ManufactorerRefUpdateView.as_view()),
    path('ref/manufacturer-ref-list/', ManufacturerRefListView.as_view(), name='ManufacturerRefList'),
    path('ref/manufacturer-ref-detail/<int:pk>/', ManufacturerRefDetailView.as_view()),
    path('ref/manufacturer-ref-delete/<int:pk>/', ManufactorerRefDeleteView.as_view()),
]
