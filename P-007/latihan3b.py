# bagaimana jika data siswa yang dimasukkan lebih dari 1?
'''
🎯 Tujuan Program:
- Bisa input lebih dari 1 siswa
- Untuk tiap siswa, bisa input beberapa mata pelajaran dan nilainya
- Menampilkan daftar hasil akhir semua siswa:
    - Nilai tiap mapel
    - Rata-rata
    - Predikat
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

print("\n=== Rangkuman Nilai Semua Siswa ===\n")
for i, siswa in enumerate(daftar_siswa, start=1):
    print(f"{i}. Nama: {siswa['nama']}")
    for mapel, nilai in siswa['nilai']:
        print(f"   - {mapel}: {nilai}")
    print(f"   Rata-rata: {siswa['rata']:.2f}")
    print(f"   Predikat : {siswa['predikat']}\n")
