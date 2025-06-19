belanja = []
total = 0

print("Masukkan daftar belanja kamu (maksimal 5 item):")

for i in range(5):
    nama = input(f"Nama barang ke-{i+1}: ")
    
    try:
        harga = int(input(f"Harga {nama}: Rp "))
    except ValueError:
        print("Harga harus angka ya! Dianggap 0.")
        harga = 0

    belanja.append((nama, harga))

print("\nDaftar belanja kamu:")
for item in belanja:
    print(f"- {item[0]}: Rp {item[1]}")
    total += item[1]

print(f"\nTotal: Rp {total}")

# Penilaian kategori
if total < 50000:
    print("Kategori: Belanja irit!")
elif total <= 100000:
    print("Kategori: Cukup lah!")
else:
    print("Kategori: Wah, boros juga 😅")
