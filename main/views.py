from django.shortcuts import render

from main.models import Experience


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


def show_experience(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)