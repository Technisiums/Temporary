from django.contrib import admin
from django.urls import path
from .views import all_books

urlpatterns = [
    path('books/', all_books, name="all_Books"),
]
