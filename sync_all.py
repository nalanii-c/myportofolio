import os
import sys
import requests
import django

# 1. Dapatkan lokasi folder saat ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Tambahkan folder saat ini DAN parent folder ke sys.path
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.dirname(BASE_DIR))

# 3. Cari settings file secara otomatis
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportofolio.settings')

try:
    django.setup()
except Exception:
    # Jika nama folder root settings beda, coba fallback
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    django.setup()

from portfolio.models import Experience  # Sesuaikan jika nama app kamu bukan 'portfolio'

LINKEDIN_URL = "https://www.linkedin.com/in/khalisha-nalani-chandra-18a693379/"

def run_sync():
    print("🚀 Memulai proses update dari terminal...")
    print(f"🔗 Mengambil data LinkedIn: {LINKEDIN_URL}")

    # Menggunakan API Microlink
    api_url = f"https://api.microlink.io/?url={LINKEDIN_URL}"
    response = requests.get(api_url)

    foto_url = None
    if response.status_code == 200:
        data = response.json().get("data", {})
        foto_info = data.get("image", {})
        foto_url = foto_info.get("url") if foto_info else None
        print(f"📸 Foto LinkedIn ditemukan: {foto_url}")
    else:
        print("⚠️ Gagal mengambil foto otomatis dari LinkedIn, tetap update link LinkedIn.")

    # Update Database Django
    experiences = Experience.objects.all()
    if not experiences.exists():
        print("⚠️ Belum ada data di database. Membuat 1 sampel data baru...")
        Experience.objects.create(
            title="Intern Staff PekRis Marcomms",
            description="Handled end-to-end video editing and thumbnail creation...",
            linkedin_url=LINKEDIN_URL,
            image_url=foto_url or ""
        )
    else:
        count = 0
        for exp in experiences:
            exp.linkedin_url = LINKEDIN_URL
            if foto_url and hasattr(exp, 'image_url'):
                exp.image_url = foto_url
            exp.save()
            count += 1
        print(f"✅ Berhasil memperbarui {count} data Experience di Database!")

if __name__ == "__main__":
    run_sync()