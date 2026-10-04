# 🚀 Personal Portfolio Website - Django

[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)]()
[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat-square&logo=django&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![Campus](https://img.shields.io/badge/Univ-Universitas%20Indonesia-blue?style=flat-square)]()

---

## 👩‍💻 Identitas Mahasiswa
| Atribut | Keterangan |
| :--- | :--- |
| **Nama** | Khalisha Nalani Chandra |
| **NPM** | 2506625041 |
| **Kelas** | PBP A |
| **Program Studi** | Sistem Informasi |
| **Hobi** | Coding & Ice Skating |

---

## 📚 Refleksi Pembelajaran
### 🎨 Tugas 1: HTML & CSS Semantik

1. Aku pake elemen semantik kayak `<section>`, `<article>`, `<header>`, sama `<nav>` buat nyusun halamannya. Bagian `<section>` aku bagi per blok utama (Profile, Education, Skills), terus tiap card di dalem gridnya (kayak riwayat pendidikan atau skill) aku bungkus pake `<article>` karena emang bisa berdiri sendiri sebagai satu unit konten. Enaknya, pas buka lagi kodenya beberapa hari kemudian, aku nggak perlu mikir lama buat nyari bagian mana yang mana. Beda banget kalau semuanya cuma `<div>` doang, pasti pusing sendiri nebak fungsinya apa.

2. Yang paling bikin ribet itu ngatur grid biar nggak berantakan pas layarnya mengecil, terutama di bagian hero (foto + identitas) yang awalnya 2 kolom. Kalau dipaksa pake ukuran fix, di HP langsung kepotong atau kegencet. Akhirnya aku akalin pake `grid-template-columns: repeat(auto-fit, minmax(...))` biar bisa nyesuain otomatis, plus nambahin media query buat ngubah layoutnya dari 2 kolom jadi numpuk satu kolom pas layarnya di bawah 600px. Prioritasku yang penting nama sama bio tetep kebaca jelas dan rapi, fotonya tinggal nyesuain ukuran atau pindah ke bawah.

3. Karena ini web statis, aku nggak bisa nambah atau ngedit konten (misal ada pengalaman baru) tanpa ngoprek langsung file HTMLnya soalnya belum ada dashboard atau form admin. Kalau datanya makin banyak, pasti bakal repot banget buat maintain satu2. Makanya di iterasi berikutnya, aku pengen simpen data2 ini (Education, Skills, Experience) di database biar bisa di render dinamis lewat template Django, jadi tinggal update data tanpa harus bongkar susunan HTML lagi.

### ⚙️ Tugas 2: Django Models & Database Migration

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

### 📝 Tugas 3: ModelForm, CSRF, & JSON API

1. Selama aku mengerjakan proyek portofolio ini, aku menggunakan `ModelForm` di Django alih2 membuat form HTML secara manual karena jauh lebih praktis dan efisien. `ModelForm` secara otomatis menghubungkan *fields* form dengan model Django (`Project`, `Experience`, `Skill`, `Education`) yang sudah kubuat, jadi aku tidak perlu menulis ulang kode HTML untuk setiap input dan melakukan validasi secara manual. Selain itu, aku juga wajib menambahkan tag `{% csrf_token %}` pada form HTML-ku untuk melindungi aplikasi dari serangan *Cross-Site Request Forgery* (CSRF), memastikan setiap pengiriman data POST (seperti saat aku menambahkan atau memperbarui data portofolio) benar2 berasal dari diriku sendiri yang sah di dalam sesi aplikasi tersebut.

2. Pada Tutorial 03, kami membahas format data JSON dan XML. Dalam pengembangan aplikasi web modern, aku melihat bahwa JSON jauh lebih disukai dibandingkan XML karena strukturnya yang jauh lebih ringan, ringkas, tidak memerlukan *closing tag* yang panjang, serta sangat mudah dibaca dan diproses secara langsung oleh JavaScript di sisi *frontend*. Hal ini membuat proses transfer data asinkron antar komponen web menjadi jauh lebih cepat dan efisien.

3. Alur yang terjadi saat aku menggunakan fungsi *view* untuk mengembalikan data portofolio (seperti data proyek atau pengalamanku) dalam bentuk JSON dimulaiFtug dengan *view* mengambil data dari *database* menggunakan *QuerySet* Django (misalnya `Project.objects.all()`). Karena objek model Django berupa kumpulan data Python yang tidak bisa langsung dibaca oleh protokol HTTP/JavaScript mentah, aku perlu melakukan proses *serialization* (mengubah objek model menjadi format standar yang bisa dibaca mesin, menggunakan *serializer* bawaan Django atau `JsonResponse`). Setelah data berhasil di *serialize* menjadi format JSON, *view* akan mengembalikan data tersebut sebagai *HTTP response* ke klien, sehingga data portofolioku bisa diakses atau diolah lebih lanjut dengan mudah oleh *frontend*.

### 🌐 Tugas 5: Web Interactivity with JavaScript

### Tugas 5

1. **Debouncing** itu teknik buat nunda eksekusi sebuah fungsi sampai user berhenti melakukan aksi (misalnya ngetik) selama jeda waktu tertentu. Kalau user masih ngetik sebelum jeda habis, timer nya di reset lagi. Di proyekku, aku pakai `setTimeout` dan `clearTimeout` dengan jeda 300 ms (`SEARCH_DEBOUNCE_DELAY`) di event `input` kolom search. Teknik ini penting di pencarian AJAX karena tanpa debounce, setiap huruf yang diketik langsung ngirim request ke `/projects/json/`. Misalnya ngetik Toy bakal ngirim 3 request (T, To, Toy), padahal yang dibutuhin cuma hasil akhirnya. Akibatnya server kerja berlebihan, dan response lama yang telat datang bisa nimpa hasil yang lebih baru sehingga tampilannya salah. Dengan debounce, request cuma dikirim sekali setelah user berhenti ngetik. Di `fetchProjects` aku juga pakai `AbortController` supaya request lama dibatalin kalau ada request baru.

2. `await` dipakai buat nunggu `fetch()` selesai dan ngasih hasil aslinya (objek `Response`), soalnya `fetch()` itu asynchronous dan langsung ngembaliin `Promise`, bukan datanya. Dengan `await`, JavaScript berhenti sebentar di baris itu (tanpa nge freeze halaman) sampai response nya datang, baru lanjut ke baris berikutnya. Kalau nggak pakai `await`, variabel `response` isinya masih `Promise` yang belum selesai, jadi `response.ok` bakal `undefined`. Di `fetchProjects`, kondisi `!response.ok` jadi true sehingga error dilempar dan yang tampil malah pesan Gagal memuat data, padahal servernya baik2 aja. Di `addProject`, kode setelah fetch (toast, tutup modal, `fetchProjects`) bakal jalan duluan sebelum server jawab, blok `finally` juga langsung jalan sehingga tombol submit aktif lagi padahal request belum kelar, dan `try/catch` nggak bakal nangkep error jaringan karena error nya baru muncul nanti di luar blok itu.

3. **XSS (Cross-Site Scripting)** itu serangan di mana penyerang nyisipin script berbahaya (misalnya `<script>` atau `<img onerror=...>`) ke input yang nanti ditampilkan di halaman, sehingga script nya jalan di browser korban. Dampaknya bisa nyuri cookie atau sesi login, ngubah tampilan halaman, atau ngelakuin aksi atas nama korban. Data lewat AJAX/JavaScript lebih rentan karena Django template otomatis nge-escape variabel `{{ }}` (autoescape), jadi `<` berubah jadi `&lt;` dan aman by default. Sedangkan di JavaScript, data dari JSON itu mentah, dan kita sendiri yang nyusun HTML pakai template literal terus dimasukin lewat `innerHTML`, yang nafsirin string sebagai HTML beneran tanpa escaping otomatis. Jadi lupa satu nilai aja bisa jadi celah. Di proyekku aku nutupnya dua lapis: `escapeHtml()` di semua nilai teks sebelum masuk `innerHTML` di `buildProjectCardElement` (toast juga pakai `textContent`), plus `strip_tags` di method `clean_<field>` pada `ModelForm` di sisi server. Pas dites, judul `<script>alert(1)</script>Halo` tersimpan jadi `alert(1)Halo`.

## 🤖 AI Disclosure & Evaluasi Kritis Perjalanan Proyek

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

### Tugas 4 (Authorization, Role Editor, & Star):

AI membantu menjelaskan cara membuat grup `Editor` beserta permission-nya lewat terminal, menyusun decorator `perm_required` untuk pengecekan hak akses di sisi server, merapikan template agar tombol create, update, dan delete hanya muncul untuk pengguna yang berhak, serta memeriksa kebocoran data pada tooltip star dan endpoint JSON.

* **Asumsi Struktur Proyek yang Meleset:** Pada Tugas 4, beberapa saran awal AI memakai nama URL dan folder yang berbeda dari proyekku, misalnya `/projects/add/` padahal routeku `/projects/create/`, atau folder `main/templates` padahal templateku ada di folder `templates/`. AI baru bisa menyesuaikan setelah aku menempelkan isi file dan output terminalnya.

* **Masalah Encoding di Windows:** Script dari AI untuk menulis file lewat PowerShell sempat membuat simbol bintang di tombol star berubah jadi `?`, dan file tes terkena karakter BOM sehingga muncul error `U+FEFF`. Masalah ini tidak terlihat dari kodenya, baru ketahuan setelah aku menjalankannya sendiri.

* **Pengujian Hak Akses Tiap Peran:** Aku membuat user `editor1` dan `biasa1` lewat shell, lalu mengecek satu per satu respons tiap peran (redirect ke login, 403, atau berhasil), dan membuka halaman `/projects/` sebagai anonim dan editor untuk memastikan tombol yang tampil sesuai hak akses.

* **Perbaikan Keamanan Data:** Aku menemukan `edit_project` yang belum dilindungi, tooltip star yang menampilkan username, dan JSON yang membocorkan ID user lewat `starred_by`, lalu memperbaikinya satu per satu. Aku juga memperbaiki URL di `test_e2e.py` dan fixture `initial_projects.json` yang fieldnya sudah tidak cocok dengan model.

### Tugas 5 (Web Interactivity with JavaScript):

AI (Claude) membantu menyusun komponen toast untuk notifikasi sukses dan error validasi dari server, menambahkan `strip_tags` pada method `clean_<field>` di `ModelForm`, memeriksa nilai teks yang disisipkan lewat JavaScript supaya di-escape, serta membantu merapikan jawaban pertanyaan reflektif tentang debouncing, `await`, dan XSS.

* **Asumsi Struktur Proyek yang Meleset:** Saran awal AI belum tahu bahwa `project.html` sudah memanggil `showToast` dengan tiga argumen (judul, pesan, tipe), sedangkan komponen toast pertama yang dibuat hanya menerima dua argumen. AI baru bisa menyesuaikan setelah aku menempelkan isi `views.py`, `forms.py`, dan `project.html`.

* **Salah Diagnosis Tombol Tambah Proyek:** Saat tombol "Tambah Proyek" hilang, awalnya aku kira kodenya terhapus. Setelah dicek lewat shell, ternyata tombol itu memang disembunyikan untuk akun tanpa izin `add_project`, dan aku tadi login dengan akun biasa.

* **Script Pengujian yang Tidak Berjalan Semestinya:** Script tes peran dari AI sempat tidak mengeluarkan hasil apa pun karena dijalankan lewat console interaktif, lalu error `UNIQUE constraint failed` karena user sementara tertinggal di database. Aku menjalankan ulang dengan versi yang membersihkan user sisa lebih dulu, lalu memastikan semua halaman berstatus 200 untuk pengunjung, user biasa, dan superuser.

* **Pengujian Mandiri XSS:** Aku mengetes judul `<script>alert(1)</script>Halo` dan memastikan hasilnya tersimpan sebagai `alert(1)Halo`, lalu mengetes `EducationForm` untuk memastikan tag juga dibuang di form lain. Saat mengetes `SkillForm`, ternyata field `category` berupa pilihan (`choices`), jadi inputnya ditolak lebih dulu oleh Django sebelum sampai ke `strip_tags`.