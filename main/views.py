from django.shortcuts import render
from main.models import Skill, Experience

<<<<<<< HEAD
#Main
=======

>>>>>>> dd5a78b (fix: restructure main app folder and add new model migrations)
def show_main(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "npm": "2506625041",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Second-Year Information Systems Undergraduate @Universitas Indonesia | Graphic Designer | Data Science Enthusiast | Figure Skater "
        ),
    }
    return render(request, "index.html", context)

#Experience
def show_experience(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

<<<<<<< HEAD
#Skill
=======
#Skills
>>>>>>> dd5a78b (fix: restructure main app folder and add new model migrations)
def show_skills(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "skills_list": Skill.objects.all(),
    }
    return render(request, "skills.html", context)