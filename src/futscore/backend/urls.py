from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('campeonatos/seriea', views.serieA, name='serieA'),
    path('campeonatos/serieb', views.serieB, name='serieB'),
]
