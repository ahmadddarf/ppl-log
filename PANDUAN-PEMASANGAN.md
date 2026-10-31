# Panduan Memasang PPL Log di iPhone

Internet hanya dibutuhkan **sekali**, saat pemasangan. Setelah itu app berjalan 100% offline.
Catatan workout-mu tidak pernah diunggah ke mana pun; yang diunggah hanya file aplikasinya.

## A. Unggah app ke GitHub Pages (sekali saja, dari laptop)

1. Buka https://github.com dan buat akun (gratis) kalau belum punya.
2. Klik tombol **+** di kanan atas, pilih **New repository**.
   - Repository name: `ppl-log`
   - Pilih **Public** (wajib untuk GitHub Pages gratis; yang terlihat publik hanya kode app, bukan datamu).
   - Klik **Create repository**.
3. Di halaman repository baru, klik tautan **uploading an existing file**.
4. Seret 5 file ini dari folder `002. WORKOUT TRACKER APPWEB` ke halaman tersebut:
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - `icon-180.png`
   - `icon-512.png`
5. Klik **Commit changes**.
6. Buka tab **Settings** di repository, lalu menu **Pages** di kiri.
   - Bagian *Build and deployment* → Source: **Deploy from a branch**
   - Branch: **main**, folder: **/ (root)** → klik **Save**.
7. Tunggu 1–2 menit, lalu muat ulang halaman Pages. Akan muncul alamat seperti:
   `https://NAMA-AKUNMU.github.io/ppl-log/`

## B. Pasang di iPhone

1. Buka alamat tadi di **Safari** (harus Safari, bukan Chrome).
2. Ketuk tombol **Share** (kotak dengan panah ke atas).
3. Gulir ke bawah, pilih **Add to Home Screen**, lalu ketuk **Add**.
4. Buka **PPL Log** dari ikon homescreen **sekali** selagi ada internet. Tunggu ±5 detik.
5. Selesai. Coba nyalakan **mode pesawat**, lalu buka app lagi: harus tetap jalan.

## C. Saat ada versi baru (setelah revisi)

1. Unggah ulang file yang berubah ke repository yang sama (**Add file → Upload files**, timpa file lama).
2. Di iPhone, buka app saat ada internet, tutup, lalu buka lagi. Versi baru aktif di pembukaan kedua.
3. Data workout tidak hilang saat app diperbarui.

## D. Jaga data tetap aman

- Data tersimpan di iPhone, di dalam app ini saja.
- **Menghapus ikon app dari homescreen akan menghapus semua catatan.**
- Lakukan **Pengaturan → Backup** secara rutin (misal seminggu sekali) dan simpan filenya ke **Files / iCloud Drive**.
- Pindah HP atau tidak sengaja terhapus: pasang ulang app, lalu **Pengaturan → Restore** dan pilih file backup.

## E. Hal yang perlu diketahui

- Bunyi "beep" di akhir timer istirahat tidak terdengar kalau iPhone dalam mode senyap; tetap muncul notifikasi hijau di layar.
- Timer tetap menghitung dengan benar walau kamu keluar dari app sebentar, tapi bunyinya baru keluar saat app dibuka lagi.
- Kalau app ditutup di tengah workout, sesi tidak hilang: buka lagi dan ketuk **Lanjutkan**.
