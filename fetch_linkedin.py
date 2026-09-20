import os
import django
import requests

# Set environment Django agar bisa akses Database langsung dari script ini
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportofolio.settings') # Sesuaikan nama folder settings kamu
django.setup()

from portfolio.models import Experience # Sesuaikan nama app & model kamu

# URL LinkedIn 
LINKEDIN_URL = "https://www.linkedin.com/in/khalisha-nalani-chandra-18a693379/"

def sync_linkedin_data():
    print("Mengambil data metadata LinkedIn...")
    api_url = f"https://api.microlink.io/?url={LINKEDIN_URL}"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json().get("data", {})
        foto_info = data.get("image", {})
        foto_url = foto_info.get("url") if foto_info else None

        print(f"URL Foto ditemukan: {foto_url}")

        # Update salah satu data Experience di Database Django secara otomatis
        experiences = Experience.objects.all()
        if experiences.exists():
            for exp in experiences:
                exp.linkedin_url = LINKEDIN_URL
                if foto_url and not exp.image_url:
                    exp.image_url = foto_url
                exp.save()
            print("✅ BERHASIL! Semua data Experience di-update otomatis di Database Django.")
        else:
            print("⚠️ Belum ada data Experience di database. Silakan buat data baru terlebih dahulu.")
    else:
        print(f"❌ Gagal mengambil data dari LinkedIn. Status: {response.status_code}")

if __name__ == "__main__":
    sync_linkedin_data()