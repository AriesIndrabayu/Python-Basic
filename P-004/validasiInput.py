# validasi input

'''
angka = input("Masukkan angka: ")
hasil = int(angka) * 2


Kalau user masukin “abc”, langsung error tuh
Solusinya? Kita cek dulu inputnya valid atau nggak.
Cara pertama: pakai .isdigit()
'''

angka = input("Masukkan angka: ")
if angka.isdigit():
    angka = int(angka)
    print("Hasil dikali dua:", angka * 2)
else:
    print("Input harus berupa angka!")

# Cara kedua: pakai try-except
try:
    angka = int(input("Masukkan angka: "))
    print("Hasil:", angka * 2)
except:
    print("Input tidak valid, harus angka!")
