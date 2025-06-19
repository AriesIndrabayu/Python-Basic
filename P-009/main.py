from input_siswa import input_data_siswa
from rekap_mapel import buat_rekap_mapel, tampilkan_rekap
from ekspor_csv import ekspor_hasil, ekspor_rekap

print("=== Program Konversi Nilai Beberapa Siswa ===\n")
daftar_siswa = input_data_siswa()

print("\n=== Rangkuman Nilai Semua Siswa ===\n")
for i, siswa in enumerate(daftar_siswa, start=1):
    print(f"🏅 Peringkat #{i} | Nama: {siswa['nama']}")
    for mapel, nilai in siswa['nilai']:
        print(f"   - {mapel}: {nilai}")
    print(f"   Rata-rata: {siswa['rata']:.2f}")
    print(f"   Predikat : {siswa['predikat']}")
    print(f"   Status   : {'LULUS' if siswa['rata'] >= 70 else 'TIDAK LULUS'}\n")

rekap_mapel = buat_rekap_mapel(daftar_siswa)
tampilkan_rekap(rekap_mapel)

ekspor_hasil(daftar_siswa)
ekspor_rekap(rekap_mapel)
