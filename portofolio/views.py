from django.shortcuts import render
from .models import Experience

def show_main(request):
    context = {
        'name': 'Khalisha Nalani Chandra',
        'npm': '2506625041',
        'study_program': 'Information Systems',
        'bio': 'Second-Year Information Systems Undergraduate @Universitas Indonesia | Graphic Designer | Data Science Enthusiast | Figure Skater',
    }
    return render(request, 'index.html', context)

def show_experience(request):
    experience_list = Experience.objects.all()
    context = {
        'name': 'Khalisha Nalani Chandra',
        'experience_list': experience_list,
    }
    return render(request, 'experience.html', context)