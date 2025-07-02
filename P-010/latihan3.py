def cetak_struk(*harga_barang, **info_pembeli):
    """
    Fungsi gabungan *args dan **kwargs untuk mencetak struk belanja.
    *args → harga barang
    **kwargs → informasi pembeli
    """
    print("=== STRUK BELANJA ===\n")
    kunci_diizinkan = ["nama", "alamat", "no_hp", "member"]

    for harga in harga_barang:
        if not isinstance(harga, (int, float)):
            print(f"❌ Harga '{harga}' tidak valid. Harus berupa angka.")
            return
        if harga < 0:
            print(f"❌ Harga '{harga}' tidak boleh negatif.")
            return

    # Informasi Pembeli
    for kunci, nilai in info_pembeli.items():
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

    print("\n=== Daftar Barang ===")
    for idx, harga in enumerate(harga_barang, start=1):
        print(f"Barang ke-{idx}: Rp{harga:,}")

    total = sum(harga_barang)
    print(f"\nTotal yang harus dibayar: Rp{total:,}")
    print("========================\n")


# Contoh penggunaan
cetak_struk(
    10000,
    5000,
    7500,
    nama="Lina",
    no_hp="08134567890",
    alamat="Jl. Merdeka 10",
    member="Tidak",
)
