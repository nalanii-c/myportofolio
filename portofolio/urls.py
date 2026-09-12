from django.contrib import admin
from django.urls import path, include

# Mendaftarkan Nama Routesnya
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
