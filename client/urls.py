from django.urls import path

from client.views import *

urlpatterns = [
    path('', Namee.as_view())
]
