# Aplikasi Kasir Sederhana
print("=== Program Kasir Sederhana ===")
total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")
    if nama_barang.lower() == "selesai":
        break

    try:
        harga = float(input(f"Masukkan harga {nama_barang}: "))
        total_belanja += harga
    except ValueError:
        print("Input harga tidak valid, coba lagi.")
        continue

print(f"\nTotal belanja: Rp {total_belanja:.0f}")

# Percabangan diskon
if total_belanja > 100000:
    diskon = total_belanja * 0.10
    total_akhir = total_belanja - diskon
    print(f"Kamu mendapat diskon 10% sebesar Rp {diskon:.0f}")
    print(f"Total yang harus dibayar: Rp {total_akhir:.0f}")
else:
    print("Maaf, kamu belum dapat diskon.")
    print(f"Total yang harus dibayar: Rp {total_belanja:.0f}")
