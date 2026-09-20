from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm
from main.models import Education, Experience, Project, Skill


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    project_list = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Khalisha Nalani Chandra",
        "project_list": project_list,
        "title_query": title_query,
    }
    return render(request, "project.html", context)


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
    return render(request, "project_form.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
    return redirect("main:show_projects")


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