from django.urls import path
from main.views import show_main, show_education, show_experience, show_skills, show_projects

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("education/", show_education, name="show_education"),
    path("experience/", show_experience, name="show_experience"),
    path("skills/", show_skills, name="show_skills"),
    path("projects/", show_projects, name="show_projects"),
]