def buat_rekap_mapel(daftar_siswa):
    rekap_mapel = {}

    for siswa in daftar_siswa:
        nama = siswa["nama"]
        for mapel, nilai in siswa["nilai"]:
            if mapel not in rekap_mapel:
                rekap_mapel[mapel] = {"nilai": nilai, "siswa": [nama]}
            else:
                if nilai > rekap_mapel[mapel]["nilai"]:
                    rekap_mapel[mapel]["nilai"] = nilai
                    rekap_mapel[mapel]["siswa"] = [nama]
                elif nilai == rekap_mapel[mapel]["nilai"]:
                    rekap_mapel[mapel]["siswa"].append(nama)

    return rekap_mapel


def tampilkan_rekap(rekap_mapel):
    print("\n=== Rekap Nilai Tertinggi per Mata Pelajaran ===\n")
    print("{:<25} {:<15} {}".format("Mata Pelajaran", "Nilai Tertinggi", "Nama Siswa"))
    print("-" * 60)
    for mapel, data in rekap_mapel.items():
        siswa_str = ", ".join(data["siswa"])
        print(f"{mapel:<25} {data['nilai']:<15} {siswa_str}")
