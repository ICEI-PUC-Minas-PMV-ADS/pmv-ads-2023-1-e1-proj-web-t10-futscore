from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('campeonatos/seriea', views.serieA, name='serieA'),
    path('campeonatos/serieb', views.serieB, name='serieB'),
    path('campeonatos/cdb/<int:fase>', views.CDB, name='CDB'),
    path('calendario', views.calendario, name='calendario'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('recover', views.recover, name='recover'),
    path('status', views.status, name='status'),
    path('profile', views.profile, name='profile'),
]