# bagaimana dibuat rekap nilai tertinggi untuk setiap mata pelajaran?

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

print("\n=== Rangkuman Nilai Semua Siswa ===\n")
for i, siswa in enumerate(daftar_siswa, start=1):
    print(f"🏅 Peringkat #{i} | Nama: {siswa['nama']}")
    for mapel, nilai in siswa['nilai']:
        print(f"   - {mapel}: {nilai}")
    print(f"   Rata-rata: {siswa['rata']:.2f}")
    print(f"   Predikat : {siswa['predikat']}")
    print(f"   Status   : {'LULUS' if siswa['rata'] >= 70 else 'TIDAK LULUS'}\n")

# Inisialisasi dict rekap
rekap_mapel = {}

# Loop semua siswa dan nilai mereka
for siswa in daftar_siswa:
    nama = siswa["nama"]
    for mapel, nilai in siswa["nilai"]:
        if mapel not in rekap_mapel:
            # Tambahkan mapel baru
            rekap_mapel[mapel] = {
                "nilai": nilai,
                "siswa": [nama]
            }
        else:
            if nilai > rekap_mapel[mapel]["nilai"]:
                # Nilai lebih tinggi, ganti
                rekap_mapel[mapel]["nilai"] = nilai
                rekap_mapel[mapel]["siswa"] = [nama]
            elif nilai == rekap_mapel[mapel]["nilai"]:
                # Nilai sama, tambahkan siswa
                rekap_mapel[mapel]["siswa"].append(nama)

# Tampilkan hasil rekap
print("\n=== Rekap Nilai Tertinggi per Mata Pelajaran ===\n")
print("{:<25} {:<15} {}".format("Mata Pelajaran", "Nilai Tertinggi", "Nama Siswa"))
print("-" * 60)
for mapel, data in rekap_mapel.items():
    siswa_str = ", ".join(data["siswa"])
    print(f"{mapel:<25} {data['nilai']:<15} {siswa_str}")

# Simpan ke file .csv
import csv

with open("hasil_nilai_siswa.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["No", "Nama", "Mata Pelajaran & Nilai", "Rata-rata", "Predikat", "Status"])

    for i, siswa in enumerate(daftar_siswa, start=1):
        # Gabungkan semua mapel dan nilainya jadi satu string
        nilai_str = ", ".join([f"{mapel}: {nilai}" for mapel, nilai in siswa['nilai']])
        status = "LULUS" if siswa['rata'] >= 70 else "TIDAK LULUS"

        writer.writerow([
            i,
            siswa['nama'],
            nilai_str,
            f"{siswa['rata']:.2f}",
            siswa['predikat'],
            status
        ])

print("📁 Data telah diekspor ke file 'hasil_nilai_siswa.csv'")

with open("rekap_nilai_tertinggi.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Mata Pelajaran", "Nilai Tertinggi", "Nama Siswa"])

    for mapel, data in rekap_mapel.items():
        siswa_str = ", ".join(data["siswa"])
        writer.writerow([mapel, data["nilai"], siswa_str])

print("✅ Rekap nilai tertinggi disimpan ke 'rekap_nilai_tertinggi.csv'")

