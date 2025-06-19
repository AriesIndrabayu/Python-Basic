belanja = []
total = 0

print("Masukkan daftar belanja kamu.")
print("Ketik 'selesai' untuk mengakhiri input.\n")

while True:
    nama = input("Nama barang: ")
    if nama.lower() == "selesai":
        break

    try:
        harga = int(input(f"Harga {nama}: Rp "))
    except ValueError:
        print("Harga harus berupa angka! Dianggap Rp 0.")
        harga = 0

    belanja.append((nama, harga))

# Menampilkan hasil
print("\n🧾 Daftar belanja kamu:")
for item in belanja:
    print(f"- {item[0]}: Rp {item[1]}")
    total += item[1]

print(f"\n💰 Total belanja: Rp {total}")

# Penilaian kategori
if total < 50000:
    print("🟢 Kategori: Belanja irit!")
elif total <= 100000:
    print("🟡 Kategori: Cukup lah!")
else:
    print("🔴 Kategori: Wah, boros juga 😅")
