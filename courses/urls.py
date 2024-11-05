from django.urls import path
from .views import home_view, multiple_answers_view, rearange_view, rearange_input_view

urlpatterns = [
    path('', home_view, name="home"),
    path('rearanjare', rearange_view, name="rearange_url"),
    path('rearanjareinput', rearange_input_view, name="rearange_input_url"),
    path('multipleanswers', multiple_answers_view, name="multiple_answers")
]
