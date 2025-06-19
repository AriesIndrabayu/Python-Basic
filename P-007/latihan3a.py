# bagaimana jika data siswa dimasukkan oleh user?

print("=== Program Konversi Nilai Mahasiswa ===\n")

# Input nama siswa
nama = input("Masukkan nama siswa: ")

# List untuk menyimpan nilai
nilai_list = []

print("\nMasukkan nilai per mata pelajaran.")
print("Ketik 'selesai' untuk mengakhiri input.\n")

while True:
    mapel = input("Nama mata pelajaran: ")
    if mapel.lower() == "selesai":
        break

    try:
        nilai = float(input(f"Nilai untuk {mapel}: "))
    except ValueError:
        print("Nilai harus berupa angka. Dianggap 0.")
        nilai = 0

    nilai_list.append((mapel, nilai))

# Hitung rata-rata
if len(nilai_list) == 0:
    print("\n⚠️ Tidak ada nilai yang dimasukkan.")
else:
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

    # Tampilkan hasil
    print(f"\n📄 Hasil Penilaian untuk {nama}")
    for i, (mapel, nilai) in enumerate(nilai_list, start=1):
        print(f"{i}. {mapel} = {nilai}")

    print(f"\n📊 Rata-rata nilai: {rata2:.2f}")
    print(f"🎖️ Predikat: {predikat}")
