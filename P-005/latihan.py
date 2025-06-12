# 🔸 Latihan 1: Cetak angka 1-10, tapi skip angka 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 🔸 Latihan 2: Input angka, stop jika user input 0
while True:
    angka = int(input("Masukkan angka: "))
    if angka == 0:
        break
    print("Kamu memasukkan:", angka)

# 🔸 Latihan 3: Hitung total dari list angka
angka = [5, 8, 3, 9]
total = 0
for a in angka:
    total += a
print("Total:", total)
