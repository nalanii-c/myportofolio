import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm
from main.permissions import perm_required
from main.models import Education, Experience, Project, Skill
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def show_projects(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Khalisha Nalani Chandra",
        "title_query": title_query,
        "form" : ProjectForm(),
    }
    return render(request, "project.html", context)

@perm_required("main.add_project")
def create_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")
    context = {
        "name": "Khalisha Nalani Chandra",
        "form": form,
    }
    return render(request, "project_form.html", context)

@perm_required("main.change_project")
def edit_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")
    context = {
        "name": "Khalisha Nalani Chandra",
        "form": form,
        "project": project,
    }
    return render(request, "edit_project.html", context)

@perm_required("main.delete_project")
def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)
    return redirect("main:show_projects")

def show_main(request):
    last_login = request.COOKIES.get("last_login", "Belum ada sesi login / Cookie tidak ditemukan")
    context = {
        "name": "Khalisha Nalani Chandra",
        "npm": "2506625041",
        "study_program": "S1 Sistem Informasi",
        "bio": "Second-Year Information Systems Undergraduate @Universitas Indonesia | Graphic Designer | Data Science Enthusiast | Figure Skater",
        "github_url": "https://github.com/nalanii-c",
        "linkedin_url": "https://www.linkedin.com/in/khalisha-nalani-chandra-18a693379/",
        "email": "chandra.nala20@gmail.com",
        "last_login": last_login,
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

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    context = {
        "name": "Khalisha Nalani Chandra",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie("last_login", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return response
    context = {
        "name": "Khalisha Nalani Chandra",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie("last_login")
    return response

@require_POST
def create_project_ajax(request):
    if not request.user.has_perm("main.add_project"):
        return JsonResponse({"message": "Anda tidak memiliki izin untuk menambahkan proyek."}, status=403)
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse({"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)}, status=201)
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
