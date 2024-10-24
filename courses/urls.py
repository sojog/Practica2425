from django.urls import path
from .views import home_view, multiple_answers_view

urlpatterns = [
    path('', home_view, name="home"),
    path('multipleanswers', multiple_answers_view, name="multiple_answers")
]
