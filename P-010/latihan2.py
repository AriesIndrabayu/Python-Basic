def cetak_info_pembeli(**info):
    """
    Fungsi untuk mencetak data pembeli secara fleksibel.
    Menggunakan **kwargs untuk menerima berbagai informasi tambahan.
    """
    kunci_diizinkan = ["nama", "alamat", "no_hp", "member"]
    print("=== Informasi Pembeli ===")
    for kunci, nilai in info.items():
        if kunci in kunci_diizinkan:
            # Validasi tiap kunci:
            if kunci == "nama":
                if (
                    not nilai.strip()
                ):  # Fungsi .strip() digunakan untuk menghapus spasi (whitespace) di awal dan akhir string.
                    print(f"❌ Nama tidak boleh kosong.")
                else:
                    print(f"Nama: {nilai}")

            elif kunci == "alamat":
                if len(nilai.strip()) < 5:
                    print(f"❌ Alamat minimal 5 karakter.")
                else:
                    print(f"Alamat: {nilai}")

            elif kunci == "no_hp":
                if nilai.startswith("08") and nilai[2:].isdigit():
                    print(f"No_hp: {nilai}")
                elif nilai.startswith("+62") and nilai[3:].isdigit():
                    print(f"No_hp: {nilai}")
                else:
                    print(
                        f"❌ No HP harus diawali '08' atau '+62' dan sisanya angka saja."
                    )
            else:
                print(f"{kunci.capitalize()}: {nilai}")
        else:
            print(f"⚠️  {kunci} tidak dikenali dan diabaikan.")

    print()  # newline


# Contoh penggunaan bebas
cetak_info_pembeli(
    nama="Bayu", no_hp="08123456789", alamat="Jl. Merdeka 10", member="Ya"
)
