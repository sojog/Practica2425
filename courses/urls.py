from django.urls import path
from .views import home_view, multiple_answers_view, rearange_view

urlpatterns = [
    path('', home_view, name="home"),
    path('rearanjare', rearange_view, name="rearange_url"),
    path('multipleanswers', multiple_answers_view, name="multiple_answers")
]
