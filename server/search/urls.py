from django.urls import path
from . import api

urlpatterns = [
    path('<str:query>', api.search, name='search'),
]
