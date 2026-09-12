<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path
=======
﻿from django.urls import path
from main.views import show_main, show_experience 

app_name = 'main'
>>>>>>> 3dd9ccd (fix: update experience template layout and styling)

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
]