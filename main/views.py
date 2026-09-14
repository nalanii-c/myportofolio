from django.shortcuts import render
from main.models import Experience, Skill, Education, Project

def show_main(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "npm": "2506625041",
        "study_program": "S1 Sistem Informasi",
        "bio": "Second-Year Information Systems Undergraduate @Universitas Indonesia | Graphic Designer | Data Science Enthusiast | Figure Skater",
        "github_url": "https://github.com/nalanii-c",
        "linkedin_url": "https://www.linkedin.com/in/khalisha-nalani-chandra-18a693379/",
        "email": "chandra.nala20@gmail.com",
    }
    return render(request, "index.html", context)

def show_education(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "education_list": Education.objects.all(),

    }
    return render(request, "education.html", context)

def show_skills(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "skills_list": Skill.objects.all(),
    }
    return render(request, "skills.html", context)

def show_experience(request):
    context = {
        "name": "Khalisha Nalani Chandra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Khalisha Nalani Chandra",
    }
    return render(request, "project.html", context)