def hitung_total(*harga_barang):
    """
    Fungsi untuk menghitung total harga dari barang-barang yang dibeli.
    Menggunakan *args agar jumlah barang bisa fleksibel.
    """
    print("=== Daftar Harga Barang ===")
    for idx, harga in enumerate(
        harga_barang, start=1
    ):  # Ini adalah perulangan yang digunakan untuk menelusuri semua elemen dalam harga_barang.

        print(f"Barang ke-{idx}: Rp{harga:,}")

    total = sum(harga_barang)
    print(f"\nTotal Belanja: Rp{total:,}\n")


# Contoh penggunaan
hitung_total(5000, 12000, 7500, 20000)
