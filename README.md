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