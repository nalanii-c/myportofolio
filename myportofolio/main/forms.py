from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput
from main.models import Project, Experience, Skill, Education

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "category": "Kategori",
            "description": "Deskripsi",
            "thumbnail": "URL Thumbnail",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Intern Staff PekRis",
                    "maxlength": 255,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "internship / volunteer",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu...",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "name",
            "proficiency",
            "category",
        ]

        labels = {
            "name": "Nama Skill",
            "proficiency": "Tingkat Keahlian",
            "category": "Kategori",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Python / Figma",
                    "maxlength": 100,
                }
            ),
            "proficiency": TextInput(
                attrs={
                    "placeholder": "Advanced / Intermediate",
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Programming / Design",
                }
            ),
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['year', 'institution', 'description']
        labels = {
            "year": "Tahun",
            "institution": "Nama Institusi",
            "description": "Deskripsi",
        }
        widgets = {
            "year": TextInput(
                attrs={
                    "placeholder": "2024 - Sekarang",
                    "maxlength": 50,
                }
            ),
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 200,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi pendidikan...",
                    "rows": 3,
                }
            ),
        }