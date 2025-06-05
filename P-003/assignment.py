nilai = 75


nilai += 5  # sekarang nilai = 80

"""
ini sama seperti:
nilai = 75
nilai = nilai  + 5 
"""

# Implementasi Dunia Nyata:
# 1. Menghitung Total Nilai / Skor
skor = 0
# Jawaban benar
skor += 10

# 2. Menghitung Total Harga di Keranjang Belanja (E-Commerce)
total_harga = 0
harga_barang = 15000

# Tambahkan 3 barang
total_harga += harga_barang * 3
# ⏩ Ini langsung terjadi saat user klik tombol “+ Tambah ke Keranjang” 
"""
memunculkan emoji di vsCode:
- Windows --> Win + .
- MacOs --> Control + Command + Spasi
"""

# 3. Menjumlahkan Data dari Sensor atau Log
total_suhu = 0
jumlah_data = 0

for suhu in [30, 31, 29, 32]:
    total_suhu += suhu
    jumlah_data += 1
# ⏩ Ini bisa kamu pakai buat mencari rata-rata suhu

# 4. Pengurangan Stok Barang (Inventory Management)
stok = 100
jumlah_dibeli = 3

stok -= jumlah_dibeli
# ⏩ Ini kejadian real saat user checkout barang

# 5. Menambah Kata ke Kalimat (String)
pesan = ""
pesan += "Halo, "
pesan += "nama kamu siapa?"
# ⏩ Berguna saat menyusun kalimat dari input yang berubah-ubah

# 6. Memproses List Secara Bertahap
keranjang = []
keranjang += ["apel"]
keranjang += ["pisang"]
# ⏩ Jadi lebih singkat dibanding .append() dalam beberapa kasus

# 7. Animasi/Game: Update Posisi Karakter
posisi_x = 0
kecepatan = 5

# Setiap frame
posisi_x += kecepatan

# ⏩ Posisi karakter diperbarui setiap waktu sesuai kecepatan