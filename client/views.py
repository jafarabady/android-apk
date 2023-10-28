from django.http import JsonResponse
from django.shortcuts import render


def book_list(request):
    books = [
        {'title': 'Book 1', 'author': 'Author 1'},
        {'title': 'Book 2', 'author': 'Author 2'},
        {'title': 'Book 3', 'author': 'Author 3'}
    ]
    return JsonResponse({'books': books})

# Create your views here.
