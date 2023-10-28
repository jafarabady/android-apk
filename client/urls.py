from django.urls import path

from client.views import book_list

urlpatterns = [
    path('books/', book_list, name='book_list'),
]
