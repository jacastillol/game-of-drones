from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.play, name='play'),
    path('winner', views.winner, name='winner'),
    path('about', views.about, name='about')
]