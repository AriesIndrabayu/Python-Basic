# 1️⃣ Perulangan menggunakan for
'''
struktur koding:
for item in koleksi:
    # blok kode

'''

# 🔶 Contoh 1: Loop terhadap List
print("\n🔶 Contoh 1: Loop terhadap List")
buah = ["apel", "pisang", "jeruk"]
for b in buah:
    print(b)
# Ini akan print semua isi list buah.

# 🔶 Contoh 2: Loop terhadap Range
print("\n🔶 Contoh 2: Loop terhadap Range")
for i in range(5):
    print(i)
    

print("\n🔶 Contoh 2.1: Loop terhadap range(start, stop, step)")
for i in range(2, 10, 2):
    print(i)


# 2️⃣ Perulangan menggunakan while
'''
struktur koding:
while kondisi:
    # blok kode

'''
# 🔷Contoh:
print("\n🔷 Contoh while")
x = 1
while x <= 5:
    print(x) # akan ngeprint nilai x selama x kurang dari samadengan 5
    x += 1
# contoh diatas setara dengan:
print("\n🔷 sama seperti ini")
for x in range(1, 6):
    print(x)

# 💭 Buktikan bahwa while itu loop tergantung kondisi dinamis
while True:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    if angka == 0:
        break
    print("Angka:", angka)
# kira-kira kapan loop akan berhenti?
'''
Contoh lain: Data dari sensor
while suhu < 100:
    suhu = baca_sensor()    # suhu diberi nilai dari fungsi sensor
    proses_data(suhu)       # memproses data dengan inputan suhu

'''

# 3️⃣ Kontrol Loop (break dan continue)
# 🔺 Contoh break
for i in range(10):
    if i == 5:  # jika memenuhi syarat ini loop akan berhenti
        break
    print(i)

# 🔻 Contoh continue
for i in range(5):
    if i == 2: # jika memenuhi syarat ini loop akan loncat ke iterasi/pengulangan berikutnya
        continue
    print(i)
