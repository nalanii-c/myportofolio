Nama  : Khalisha Nalani Chandra
NPM   : 2506625041
Kelas : PBP A

Hobi : Coding & Ice Skating

### Tugas 1

1. Aku pake elemen semantik kayak `<section>`, `<article>`, `<header>`, sama `<nav>` buat nyusun halamannya. Bagian `<section>` aku bagi per blok utama (Profile, Education, Skills), terus tiap card di dalem gridnya (kayak riwayat pendidikan atau skill) aku bungkus pake `<article>` karena emang bisa berdiri sendiri sebagai satu unit konten. Enaknya, pas buka lagi kodenya beberapa hari kemudian, aku nggak perlu mikir lama buat nyari bagian mana yang mana. Beda banget kalau semuanya cuma `<div>` doang, pasti pusing sendiri nebak fungsinya apa.

2. Yang paling bikin ribet itu ngatur grid biar nggak berantakan pas layarnya mengecil, terutama di bagian hero (foto + identitas) yang awalnya 2 kolom. Kalau dipaksa pake ukuran fix, di HP langsung kepotong atau kegencet. Akhirnya aku akalin pake `grid-template-columns: repeat(auto-fit, minmax(...))` biar bisa nyesuain otomatis, plus nambahin media query buat ngubah layoutnya dari 2 kolom jadi numpuk satu kolom pas layarnya di bawah 600px. Prioritasku yang penting nama sama bio tetep kebaca jelas dan rapi, fotonya tinggal nyesuain ukuran atau pindah ke bawah.

3. Karena ini web statis, aku nggak bisa nambah atau ngedit konten (misal ada pengalaman baru) tanpa ngoprek langsung file HTMLnya soalnya belum ada dashboard atau form admin. Kalau datanya makin banyak, pasti bakal repot banget buat maintain satu2. Makanya di iterasi berikutnya, aku pengen simpen data2 ini (Education, Skills, Experience) di database biar bisa di render dinamis lewat template Django, jadi tinggal update data tanpa harus bongkar susunan HTML lagi.

## AI Disclosure

Aku sempet pake Claude buat bantu nyiapin kerangka HTML di section Education dan Skills, sekaligus nentuin basic CSS-nya (grid layout, warna, sama efek hover) biar stylenya tetep senada sama desain dari Tutorial 01. Aku juga sempet diskusi buat dapet gambaran awal jawaban reflektif di atas.

Tapi untuk pengerjaannya, isi datanya (riwayat pendidikan, skill, deskripsi) full aku isi sendiri, narasinya aku tulis ulang pake bahasaku sendiri, visualnya aku tes langsung di browser termasuk cek responsivitas mobilenya, dan proses commit sampai push ke GitHub juga aku handle sendiri.



#TUGAS 2

### 1. Alur Request Halaman Portofolio Baru
Waktu aku kemarin ngetes nambahin atau buka halaman portofolio, alurnya jalan kayak gini:
* **Browser**: Kirim HTTP request (`GET /portfolio/`) dari browser pengguna ke server.
* **Project `urls.py` (`myportofolio/urls.py`)**: Menerima request di tingkat root, lalu ngecek pola URL (`path('portfolio/', include('portfolio.urls'))`) buat ngelempar requestnya ke routing milik aplikasi spesifik.
* **App `urls.py` (`portfolio/urls.py`)**: Mencocokkan path lanjutan (misalnya `path('', views.portfolio_list, name='list')`) buat dipetakan ke fungsi view yang bener.
* **View (`views.py`)**: Fungsi `portfolio_list` dipanggil. Di sini logicnya jalan, biasanya manggil model buat ngambil data (`Project.objects.all()`).
* **Model (`models.py`)**: Berkomunikasi sama database (SQLite/PostgreSQL) buat ngambil record data portofolio.
* **Template (`templates/...`)**: Data dari view dilempar ke file HTML (`render(request, 'portfolio/list.html', context)`), di-compile sama Jinja/Django templating engine, lalu hasilnya dikirim balik ke browser sebagai HTML jadi.

### 2. Kenapa Data Portofolio Harus Disimpan di Model (Bukan Hardcode di Template)?
Kemarin pas deploy ke PWS dan ngurusin data statis/dinamis, kebaca banget bedanya:
* **Maintainability**: Kalau data project (nama, deskripsi, tech stack) ditulis langsung di HTML template, tiap ada project baru aku harus edit file HTMLnya satu2. Pakai model, data tinggal ditambah lewat admin panel atau database tanpa nyentuh struktur HTML.
* **Scalability**: Satu template `detail.html` bisa dipakai buat nampung ribuan data portofolio berbeda cukup dengan ganti context query (`get_object_or_404(Project, pk=pk)`). Kalau hardcode, harus bikin file HTML baru terus buat tiap proyek.
* **Separation of Concerns**: Logika penyimpanan/struktur data terpisah dari visualisasi. Pas kemarin PWS redeploy/reset data, lebih gampang manage lewat fixture/migration ketimbang bongkar markup template.

### 3. Perbedaan `makemmigrations` vs `migrate` & Contoh Kasus
* **`python manage.py makemmigrations`**: Perintah buat scan perubahan di `models.py` (kayak nambah field baru `image = models.ImageField(...)` atau bikin model `Project`), lalu generate file migrasi baru (di folder `migrations/0002_auto_...py`) sebagai *blueprint* perubahan skema database. Belum nyentuh database sama sekali.
* **python manage.py migrate**: Perintah buat menerapkan blueprint dari file migrasi tadi ke database fisik (bikintabel baru, alter column, dll.). Kemarin pas pertama kali setup PWS atau nambah field kategori di portfolio, kalau cuma `makemmigrations` doang, database di server tetep error/kolom belum kebaca sampai `migrate` dijalankan.

**Contoh Kasus Nyata di Proyek Ini**:
Waktu aku nambahin field `featured = models.BooleanField(default=False)` di model `Project` buat nandain portofolio unggulan:
1. Jalankan `python manage.py makemmigrations` $\rightarrow$ Django ngebuat file `0002_project_featured.py`.
2. Jalankan `python manage.py migrate` $\rightarrow$ tabel `portfolio_project` di SQLite/database beneran ketambahan kolom `featured`.

### Tugas 3

1. Selama aku mengerjakan proyek portofolio ini, aku menggunakan `ModelForm` di Django alih2 membuat form HTML secara manual karena jauh lebih praktis dan efisien. `ModelForm` secara otomatis menghubungkan *fields* form dengan model Django (`Project`, `Experience`, `Skill`, `Education`) yang sudah kubuat, jadi aku tidak perlu menulis ulang kode HTML untuk setiap input dan melakukan validasi secara manual. Selain itu, aku juga wajib menambahkan tag `{% csrf_token %}` pada form HTML-ku untuk melindungi aplikasi dari serangan *Cross-Site Request Forgery* (CSRF), memastikan setiap pengiriman data POST (seperti saat aku menambahkan atau memperbarui data portofolio) benar2 berasal dari diriku sendiri yang sah di dalam sesi aplikasi tersebut.

2. Pada Tutorial 03, kami membahas format data JSON dan XML. Dalam pengembangan aplikasi web modern, aku melihat bahwa JSON jauh lebih disukai dibandingkan XML karena strukturnya yang jauh lebih ringan, ringkas, tidak memerlukan *closing tag* yang panjang, serta sangat mudah dibaca dan diproses secara langsung oleh JavaScript di sisi *frontend*. Hal ini membuat proses transfer data asinkron antar komponen web menjadi jauh lebih cepat dan efisien.

3. Alur yang terjadi saat aku menggunakan fungsi *view* untuk mengembalikan data portofolio (seperti data proyek atau pengalamanku) dalam bentuk JSON dimulai dengan *view* mengambil data dari *database* menggunakan *QuerySet* Django (misalnya `Project.objects.all()`). Karena objek model Django berupa kumpulan data Python yang tidak bisa langsung dibaca oleh protokol HTTP/JavaScript mentah, aku perlu melakukan proses *serialization* (mengubah objek model menjadi format standar yang bisa dibaca mesin, menggunakan *serializer* bawaan Django atau `JsonResponse`). Setelah data berhasil di *serialize* menjadi format JSON, *view* akan mengembalikan data tersebut sebagai *HTTP response* ke klien, sehingga data portofolioku bisa diakses atau diolah lebih lanjut dengan mudah oleh *frontend*.



## 🤖 AI Disclosure & Evaluasi Kritis Perjalanan Proyek (Tugas 1 - 3)

Dalam pengembangan portofolio web berbasis Django ini dari awal hingga tahap implementasi form dan JSON API, aku berkolaborasi dengan Gemini sebagai *AI personal collaborator*. 

Berikut adalah rangkuman peran AI serta evaluasi kritis selama pengerjaan Tugas 1 hingga Tugas 3:

### 1. Peran AI dalam Setiap Tahapan
* **Tugas 1 (HTML & CSS Semantik):** AI membantu memberikan referensi kerangka struktur elemen semantik (`<section>`, `<article>`, `<nav>`) serta *best practice* dalam mendesain *grid layout* yang responsif menggunakan *media queries*.

* **Tugas 2 (Django Models & Migrations):** AI mendampingi proses perancangan struktur model (`Project`, `Experience`, `Skill`, `Education`) serta menjelaskan perbedaan esensial antara `makemmigrations` dan `migrate` saat menerapkannya ke database.

* **Tugas 3 (ModelForm, CSRF, & JSON API):** AI membantu menyusun draf awal kelas `ModelForm` untuk masing2 model serta logika serialisasi data *query set* Django menjadi format JSON untuk kebutuhan asinkron.

### 2. Analisis Kritis terhadap Keterbatasan AI
Meskipun sangat membantu mempercepat penulisan draf kode, AI memiliki beberapa keterbatasan nyata selama proses pengembangan:

* **Ketidaksesuaian Konteks Lokal:** Kode *boilerplate* form yang dihasilkan AI seringkali menggunakan nama *field* generik yang tidak sinkron secara langsung dengan struktur model asliku (misalnya pada atribut `proficiency` di model *Skill* atau `year` di *Education*).

* **Kendala Lingkungan Deployment (PWS):** AI terkadang memberikan asumsi konfigurasi database lokal, sehingga ketika di deploy ke server PWS sempat terjadi *operational error* atau *timeout* akibat perbedaan variabel lingkungan (*environment variables*) yang harus diatasi secara manual melalui penyesuaian konfigurasi *settings.py*.

### 3. Perbaikan dan Kontrol Manual yang Dilakukan
Aku tidak menelan mentah2 seluruh keluaran kode dari AI. Kontrol penuh tetap berada di tanganku melalui langkah2 perbaikan manual berikut:

* **Validasi dan Penyesuaian Field Form:** Memeriksa ulang file `forms.py` agar secara presisi mengecualikan *field* `id` dan *timestamp*, serta memastikan *widgets* dan *labels* sesuai dengan model Django yang kubuat sendiri.

* **Debugging Mandiri:** Menganalisis pesan *error* di terminal secara mandiri, memperbaiki kesalahan *mapping* URL dan view, serta menjalankan perintah *migration* serta *testing* secara berulang hingga aplikasi berjalan mulus tanpa error.

* **Penulisan Narasi Refleksi:** Seluruh jawaban refleksi konseptual (mulai dari alasan pemilihan elemen semantik, alur HTTP request, hingga perbandingan JSON vs XML) disusun sepenuhnya menggunakan pemahaman dan bahasaku sendiri.