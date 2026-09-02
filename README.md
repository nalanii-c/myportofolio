Nama  : Khalisha Nalani Chandra
NPM   : 2506625041
Kelas : PBP A

Hobi : Coding & Ice Skating

### Tugas 1

1. Saya pakai elemen semantik kayak `<section>`, `<article>`, `<header>`, sama `<nav>` buat nyusun halamannya. `<section>` saya pisah per bagian utama (Profile, Education, Skills), sedangkan tiap kartu di dalam grid (kayak tiap riwayat pendidikan atau tiap skill) saya bungkus pakai `<article>` karena masing2 item itu sebenarnya bisa berdiri sendiri sebagai satu unit konten. Enaknya, pas saya buka lagi kode HTML-nya beberapa hari kemudian, saya nggak perlu mikir lama buat inget bagian mana yang mana—beda kalau semuanya cuma `<div>` polos, pasti saya lupa `<div>` ini fungsinya apa.

2. Yang paling bikin ribet itu ngatur grid biar nggak berantakan pas layar mengecil, khususnya bagian hero (foto + identitas) yang tadinya 2 kolom. Kalau saya paksa pakai lebar kolom tetap, di HP jadi kepotong atau kegencet. Saya akhirnya pakai `grid-template-columns: repeat(auto-fit, minmax(...))` biar kolomnya nyesuain otomatis, terus tambahin media query buat ngerubah susunan grid dari 2 kolom jadi numpuk 1 kolom pas layar di bawah 600px. Yang saya prioritasin: nama & bio harus tetep kebaca penuh, foto boleh mengecil atau pindah urutan ke bawah kalau perlu.

3. Karena static web, saya nggak bisa nambah/edit konten (misal nambah satu pengalaman baru) tanpa langsung ngoprek kode HTML-nya—nggak ada tempat kayak form atau admin panel buat itu. Kalau kontennya makin banyak ke depannya, ini bakal ribet banget maintain-nya satu2. Makanya di iterasi berikutnya saya pengen data2 ini (Education, Skills, Experience) disimpen di database, terus ditampilin lewat template Django secara dinamis, biar bisa nambah/edit konten tanpa harus bongkar HTML tiap kali.

## AI Disclosure

Saya pakai Claude buat bantu bikin kerangka HTML section Education dan Skills, plus CSS-nya (grid layout, warna, hover effect) biar gayanya nyambung sama desain yang udah saya buat di Tutorial 01. Selain itu saya juga diskusi sama Claude buat nyusun draf awal jawaban reflektif di atas.

Yang saya kerjain sendiri: isi semua datanya (riwayat pendidikan, skill, deskripsi), saya edit ulang teksnya biar sesuai fakta dan gaya nulis saya, saya tes tampilannya di browser (termasuk versi mobile), dan commit + push ke GitHub saya lakuin sendiri.
