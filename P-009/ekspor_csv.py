import csv

def ekspor_hasil(daftar_siswa):
    with open("hasil_nilai_siswa.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Nama", "Mata Pelajaran & Nilai", "Rata-rata", "Predikat", "Status"])
        for i, siswa in enumerate(daftar_siswa, start=1):
            nilai_str = ", ".join([f"{mapel}: {nilai}" for mapel, nilai in siswa['nilai']])
            status = "LULUS" if siswa['rata'] >= 70 else "TIDAK LULUS"
            writer.writerow([i, siswa['nama'], nilai_str, f"{siswa['rata']:.2f}", siswa['predikat'], status])
    print("📁 Data telah diekspor ke file 'hasil_nilai_siswa.csv'")


def ekspor_rekap(rekap_mapel):
    with open("rekap_nilai_tertinggi.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Mata Pelajaran", "Nilai Tertinggi", "Nama Siswa"])
        for mapel, data in rekap_mapel.items():
            siswa_str = ", ".join(data["siswa"])
            writer.writerow([mapel, data["nilai"], siswa_str])
    print("✅ Rekap nilai tertinggi disimpan ke 'rekap_nilai_tertinggi.csv'")
