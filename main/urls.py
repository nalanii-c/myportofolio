from django.urls import path
from main.views import (
    show_projects, 
    create_project, 
    edit_project, 
    delete_project, 
    show_experience, 
    show_main, 
    show_education, 
    show_skills
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('education/', show_education, name='show_education'),
    path('skills/', show_skills, name='show_skills'),
    path('projects/', show_projects, name='show_projects'),
    path('projects/create/', create_project, name='create_project'),
    path('projects/edit/<str:id>/', edit_project, name='edit_project'),
    path('projects/delete/<str:id>/', delete_project, name='delete_project'),
]
