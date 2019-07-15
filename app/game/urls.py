from django.urls import path, include
from rest_framework.routers import DefaultRouter

from game import views


router = DefaultRouter()
router.register('players', views.PlayerViewSet)

app_name = 'game'

urlpatterns = [
    path('', include(router.urls))
]
