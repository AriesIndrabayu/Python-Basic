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
    if float(nilai_input): # ini akan terjadi error jika yang diinputkan bukan angka (misalnya abc)
        print("yang anda inputkan berupa desimal")
        print(f"Nilai kamu: {nilai_input}")
    else:
        print("Input tidak valid tolong masukkan angka.")
        
    # solusinya: blok if dan else diatas dengan:
    try:
        float(nilai_input)
        print("Yang anda inputkan berupa desimal")
        print(f"Nilai kamu: {nilai_input}")
    except ValueError:
        print("Input tidak valid, tolong masukkan angka.")
    
# Opsi-2 menggunakan try except yang lebih ringkas 
try:
    nilai_input = input("Riset Opsi 2 Masukkan angka: ")
    nilai_float = float(nilai_input)
    if nilai_float.is_integer(): # cek apakah integer?
        print("Yang anda inputkan berupa integer")
    else:
        print("Yang anda inputkan berupa desimal")
except ValueError:
    print("Input tidak valid, tolong masukkan angka.")

'''
penjelasan opsi 1 dan 2:
kenapa yang di cek pertama pada kondisi if bukan desimal dulu .isdecimal()?
Karena integer itu subset dari float, maka:
Lebih aman: cek integer dulu → baru float → baru invalid.
'''
