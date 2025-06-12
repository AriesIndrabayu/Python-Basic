'''
Buat program yang menerima input angka dan mencetak:
"Bilangan positif" kalau lebih dari 0
"Bilangan negatif" kalau kurang dari 0
"Nol" kalau nilainya 0

'''

angka = int(input("Masukkan angka: "))

# Opsi 1:
if angka > 0:
    print("Bilangan positif")
elif angka < 0:
    print("Bilangan negatif")
else:
    print("Nol")


# Opsi 2:
if angka.lstrip('-').isdigit():
    angka = int(angka)
    if angka > 0:
        print("Bilangan Positif")
    elif angka < 0:
        print("Bilangan Negatif")
    else:
        print("Nol")
else:
    print("Input harus berupa angka!")
