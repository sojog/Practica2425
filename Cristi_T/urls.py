from django.urls import path
from .views import home_view, potriveste_view, flash_view

urlpatterns = [
    path('', home_view, name="home"),
    path('potriveste', potriveste_view, name="potriveste_url"),
    path('flash', flash_view, name="flashcards_url")
]