print("=== Program Konversi Nilai Mahasiswa ===\n")

daftar_siswa = []
semua_mapel = set()
rekap_mapel = {}

while True:
    nama = input("\nMasukkan nama siswa (atau ketik 'selesai' untuk berhenti): ")
    if nama.lower() == "selesai":
        break
    
    nilai_dict = {}
    print(f"\nMasukkan nilai untuk {nama}")
    print("Ketik 'selesai' jika tidak ada lagi mata pelajaran.\n")

    while True:
        mapel = input(" Nama mata pelajaran: ")
        if mapel.lower() == "selesai":
            break
        
        try:
            nilai = float(input(f" Nilai untuk {mapel}: "))
            # {'IPA': 85, IPS: 90}
        except ValueError:
            print(" Nilai tidak valid, dianggap 0.")
            nilai = 0
        
        nilai_dict[mapel] = nilai
        semua_mapel.add(mapel)
        
        if mapel not in rekap_mapel:
            rekap_mapel[mapel] = []
        rekap_mapel[mapel].append(nilai)
    
    if len(nilai_dict) == 0:
        print(f"Tidak ada nilai untuk {nama}. Lewati siswa ini.\n")
        continue
    
    # Hitung rata-rata:
    total = sum(nilai_dict.values())
    rata2 = total / len(nilai_dict)
    
    # Tentukan predikat
    if rata2 >= 90:
        predikat = "A (Sangat Baik)"
    elif rata2 >= 80:
        predikat = "B (Baik)"
    elif rata2 >= 70:
        predikat = "C (Cukup)"
    else:
        predikat = "D (Perlu Perbaikan)"


    daftar_siswa.append({
        "nama": nama,
        "nilai": nilai_dict,
        "rata": rata2,
        "predikat": predikat
    })

# Urutkan berdasarkan rata-rata tertinggi
daftar_siswa = sorted(daftar_siswa, key=lambda x: x['rata'], reverse=True)
print("\n=== Rangkuman Nilai Semua Siswa ===\n")
for i, siswa in enumerate(daftar_siswa, start=1):
    print(f"🏅 Peringkat #{i} | Nama: {siswa['nama']}")
    for mapel, nilai in siswa['nilai'].items():
        print(f"   - {mapel}: {nilai}")
    print(f"   Rata-rata: {siswa['rata']:.2f}")
    print(f"   Predikat : {siswa['predikat']}")
    print(f"   Status   : {'LULUS' if siswa['rata'] >= 70 else 'TIDAK LULUS'}\n")


# Rekap nilai rata-rata per mata pelajaran
print("=== Rangkuman Nilai per Mata Pelajaran ===\n")
for mapel in sorted(semua_mapel):
    nilai_mapel = rekap_mapel.get(mapel, [])
    rata_mapel = sum(nilai_mapel) / len(nilai_mapel) if nilai_mapel else 0
    print(f"- {mapel}: Rata-rata {rata_mapel:.2f} dari {len(nilai_mapel)} siswa")