def input_data_siswa():
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

        if not nilai_list:
            print(f"⚠️ Tidak ada nilai untuk {nama}. Lewati siswa ini.\n")
            continue

        total = sum(n for _, n in nilai_list)
        rata2 = total / len(nilai_list)

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
            "nilai": nilai_list,
            "rata": rata2,
            "predikat": predikat
        })

    return sorted(daftar_siswa, key=lambda x: x['rata'], reverse=True)
