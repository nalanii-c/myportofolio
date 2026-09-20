import requests
from django.core.management.base import BaseCommand
from portfolio.models import Experience  # Sesuaikan jika nama app bukan portfolio

class Command(BaseCommand):
    help = 'Mengambil data LinkedIn dan meng-update model Experience'

    def handle(self, *args, **options):
        linkedin_url = "https://www.linkedin.com/in/khalisha-nalani-chandra-18a693379/"
        self.stdout.write(f"🚀 Mengambil data dari LinkedIn: {linkedin_url}")

        # Mengambil foto metadata via API Microlink
        api_url = f"https://api.microlink.io/?url={linkedin_url}"
        res = requests.get(api_url)
        
        foto_url = None
        if res.status_code == 200:
            data = res.json().get("data", {})
            foto_info = data.get("image", {})
            foto_url = foto_info.get("url") if foto_info else None

        # Update database
        experiences = Experience.objects.all()
        if not experiences.exists():
            self.stdout.write(self.style.WARNING("⚠️ Belum ada data Experience di database."))
            return

        for exp in experiences:
            exp.linkedin_url = linkedin_url
            if foto_url and hasattr(exp, 'image_url'):
                exp.image_url = foto_url
            exp.save()

        self.stdout.write(self.style.SUCCESS(f"✅ Berhasil memperbarui {experiences.count()} data Experience!"))