peserta = []

print("Masukkan nama peserta (maksimal 5):")
while len(peserta) < 5:
    nama = input("> ")
    if nama in peserta:
        print("Nama sudah terdaftar!")
        continue
    peserta.append(nama)

print("Kuota penuh! Berikut daftar peserta:")
for i, p in enumerate(peserta, start=1):
    print(f"{i}. {p}")
