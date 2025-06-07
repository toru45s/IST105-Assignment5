from django.urls import path
from .views import puzzle_view

urlpatterns = [
    path('', puzzle_view, name='puzzle'),
]
