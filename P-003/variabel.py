# Variabel dengan tipe data string
nama = "Bayu"
# Variabel dengan tipe data integer
umur = 20
# Variabel dengan tipe data float
tinggi = 165.5

nama = 12 # Ini sih gak error, tapi sangat tidak disarankan!
print("\nData Ke-1: ")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)

"""_summary_
Tips Pentng:
Kalo kita pengen jaga data lebih ketat, nanti di Python bisa pakai type hint. Contoh...
"""
print("\nData Ke-2: ")

namaku: str = "Dudung"
namaku = 123
umur: int = 45
tinggi = 170

print("Nama:", namaku)
print("Umur:", umur)
print("Tinggi:", tinggi)

"""_summary_
aturan penamaan:
- Tidak boleh diawali angka: 1nama = "Faiz"
- Tidak boleh mengandung spasi: nama lengkap = "Azzam Maulana Dzakwan"
- Tidak boleh pakai karakter selain huruf, angka, dan underscore: 
   nama-lengkap = "Fadil"
   nama@123 = "Abdullah"
- Tidak boleh memakai kata kunci (keyword) Python:
    def = 5
    if = "tes"
    Contoh keyword Python yang tidak boleh dipakai:
    False, True, None, and, or, not, if, else, elif, for, while, break, continue,
    class, def, return, import, from, global, pass, raise, try, except, finally, lambda, dan lain-lain.
    
- Tidak membedakan besar kecil huruf secara tidak konsisten
    Nama ≠ nama ≠ NAMA
    Kalau kamu nulis:
    nama = "Bayu"
    print(Nama)  # ❌ ERROR! Variabel 'Nama' tidak ditemukan
    
    Konsisten pakai penulisan, misalnya selalu lowercase:
    nama = "Bayu"
    print(nama)  # ✅
    
Best Practice Penamaan Variabel
- Gunakan huruf kecil dan underscore jika perlu pisahkan kata, contoh:
    total_harga = 50000
    nama_barang = "Kopi"
- PascalCase (atau juga disebut UpperCamelCase)
    Ciri-cirinya:
    - Setiap kata dimulai dengan huruf kapital
    - Tidak ada underscore antar katanya
    - Contoh:
        NamaBarang
        TotalHarga
        DataPengguna
    
    🧠 Jadi, apakah boleh pakai PascalCase untuk variabel?
    Secara teknis: boleh — Python tidak akan error.
    Tapi secara konvensi PEP 8 (gaya penulisan resmi Python):
    - Variabel dan nama fungsi disarankan pakai snake_case
    - Class disarankan pakai PascalCase
    Contoh sesuai konvensi PEP 8:
    # Variabel dan fungsi (snake_case)
    nama_barang = "Kopi"
    total_harga = 25000

    def hitung_diskon(harga):
        return harga * 0.9

    # Class (PascalCase)
    class DataPengguna:
        pass

- Gunakan nama yang deskriptif dan jelas
    s = 60        # ❌ Kurang jelas
    kecepatan = 60  # ✅ Lebih informatif
    
Panduan Gaya Penulisan Python (PEP 8)
PEP 8 adalah panduan resmi penulisan kode Python agar rapi, konsisten, dan mudah dibaca.
1. Penamaan Variabel, Penamaan Fungsi --> Gunakan gaya snake_case
    nama_barang = "Kopi"
    def hitung_diskon(harga):
        return harga * 0.9
    
2. Penamaan Kelas --> Gunakan PascalCase (UpperCamelCase)
    class DataPengguna:
        pass
3. Penamaan Konstanta --> gunakan UPPER_CASE
    PI = 3.14
    MAX_LOGIN = 5
    
4. Gunakan Spasi yang Rapi
    # ✅ Benar
    x = 10
    y = x + 5

    # ❌ Hindari
    x=10
    y=x+5
"""