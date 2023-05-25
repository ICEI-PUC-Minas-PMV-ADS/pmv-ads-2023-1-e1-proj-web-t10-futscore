from django.contrib import admin
from django.urls import path, include
import backend.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(backend.urls))
]
