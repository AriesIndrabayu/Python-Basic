# validasi input

'''
angka = input("Masukkan angka: ")
hasil = int(angka) * 2


Kalau user masukin “abc”, langsung error tuh
Solusinya? Kita cek dulu inputnya valid atau nggak.
Cara pertama: pakai .isdigit()
'''
# Cara pertama: pakai .isdigit()
print("==== menggunakan .isdigit()")
nilai_input = input("Masukkan angka ke-1: ")
if nilai_input.isdigit():
    angka = int(nilai_input)
    print("Hasil dikali dua:", angka * 2)
else:
    print("Input harus berupa angka!")

# Cara kedua: pakai try-except
print("==== menggunakan try-except")
try:
    angka = int(input("Masukkan angka ke-2: "))
    print("Hasil:", angka * 2)
except:
    print("Input tidak valid, harus angka!")
    
# Bagaimana jika yang diinputkan boleh integer atau desimal?
# Opsi-1 menggunakan try except
print("==== Riset kasus baru boleh integer atau desimal")
try:
    nilai_input = input("Riset Opsi 1 Masukkan angka: ")
    int(nilai_input)
    print("yang anda inputkan berupa integer")
    print(f"Nilai kamu: {nilai_input}")
except ValueError:
    # ini akan terjadi error jika yang diinputkan bukan angka (misalnya abc)
    if float(nilai_input):
        print("yang anda inputkan berupa desimal")
        print(f"Nilai kamu: {nilai_input}")
    else:
        print("Input tidak valid tolong masukkan angka.")
        
    # solusinya: untuk baris 35-39 ganti dengan:
    try:
        float(nilai_input)
        print("Yang anda inputkan berupa desimal")
        print(f"Nilai kamu: {nilai_input}")
    except ValueError:
        print("Input tidak valid, tolong masukkan angka.")
    
# Opsi-2 menggunakan try except yang lebih ringkas 
try:
    nilai_float = float(nilai_input)
    if nilai_float.is_integer():
        print("Yang anda inputkan berupa integer")
    else:
        print("Yang anda inputkan berupa desimal")
except ValueError:
    print("Input tidak valid, tolong masukkan angka.")
