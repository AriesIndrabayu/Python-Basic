📁 Struktur Folder Utama
frontend/
├── app.py <-- File utama Flask
├── requirements.txt <-- Daftar dependensi
├── static/
│ ├── css/style.css <-- Style CSS
│ └── js/script.js <-- JavaScript (kemungkinan untuk interaksi UI)
├── templates/
│ ├── layout.html <-- Template dasar
│ └── index.html <-- Tampilan utama daftar catatan

Target:

1. aktifkan tombol pencarian untuk fitur
   - pencarian
   - tampilkan jumlah record perhalaman
   - tampilkan yang aktif dan nonaktif:
     - aktif --> data yang belum di softdelete
     - nonaktif --> data yang sudah di softdelete
   - fungsi sortby
2. aktifkan tombol pagination
3. aktifkan fitur tombol tambah data
4. aktifkan fitur tombol edit
5. aktifkan fitur tombol hapus --> ini untuk softdelete
6. aktifkan tombol restore dan force delete:
   untuk memunculkan tombol restore dan forcedelete yaitu ketika user memilih tampilan data yang non aktif.
