# bagaimana jika dibuat sorting data siswa yang mempunyai nilai rata-rata tertinggi paling atas?

'''
Kita cukup menyortir list daftar_siswa berdasarkan key "rata" dengan sorted() dan reverse=True agar yang nilai rata-ratanya paling tinggi muncul di atas.
'''

print("=== Program Konversi Nilai Beberapa Siswa ===\n")

# List untuk menyimpan data semua siswa
daftar_siswa = []

while True:
    nama = input("Masukkan nama siswa (atau ketik 'selesai' untuk berhenti): ")
    if nama.lower() == "selesai":
        break

    nilai_list = []
    print(f"\nMasukkan nilai untuk {nama}")
    print("Ketik 'selesai' jika tidak ada lagi mata pelajaran.\n")

    while True:
        mapel = input("  Nama mata pelajaran: ")
        if mapel.lower() == "selesai":
            break

        try:
            nilai = float(input(f"  Nilai untuk {mapel}: "))
        except ValueError:
            print("  Nilai tidak valid, dianggap 0.")
            nilai = 0

        nilai_list.append((mapel, nilai))

    if len(nilai_list) == 0:
        print(f"⚠️ Tidak ada nilai untuk {nama}. Lewati siswa ini.\n")
        continue

    # Hitung rata-rata
    total = sum([n[1] for n in nilai_list])
    rata2 = total / len(nilai_list)

    # Tentukan predikat
    if rata2 >= 90:
        predikat = "A (Sangat Baik)"
    elif rata2 >= 80:
        predikat = "B (Baik)"
    elif rata2 >= 70:
        predikat = "C (Cukup)"
    else:
        predikat = "D (Perlu Perbaikan)"

    # Simpan semua data siswa ke list utama
    daftar_siswa.append({
        "nama": nama,
        "nilai": nilai_list,
        "rata": rata2,
        "predikat": predikat
    })

# Urutkan siswa berdasarkan nilai rata-rata tertinggi
daftar_siswa = sorted(daftar_siswa, key=lambda x: x['rata'], reverse=True)

'''
sorted(...)
Fungsi bawaan Python yang digunakan untuk mengurutkan elemen dalam sebuah list dan mengembalikan list baru yang sudah terurut.

key=lambda x: x['rata']
Ini bagian yang menentukan patokan pengurutan.
lambda x: x['rata'] adalah fungsi kecil anonim (tanpa nama) yang:

    - menerima satu item dari daftar_siswa (yaitu dictionary siswa),
    - lalu mengambil nilai dari kunci 'rata' (nilai rata-rata siswa itu),
    - jadi misalnya kalau x = {'nama': 'Ayu', 'rata': 85}, maka x['rata'] adalah 85.
    
reverse=True
Menandakan bahwa urutannya dibalik, jadi:
    - nilai tertinggi muncul di atas
    - nilai terendah muncul di bawah.
'''

print("\n=== Rangkuman Nilai Semua Siswa ===\n")
for i, siswa in enumerate(daftar_siswa, start=1):
    print(f"🏅 Peringkat #{i} | Nama: {siswa['nama']}")
    for mapel, nilai in siswa['nilai']:
        print(f"   - {mapel}: {nilai}")
    print(f"   Rata-rata: {siswa['rata']:.2f}")
    print(f"   Predikat : {siswa['predikat']}")
    print(f"   Status   : {'LULUS' if siswa['rata'] >= 70 else 'TIDAK LULUS'}\n")
