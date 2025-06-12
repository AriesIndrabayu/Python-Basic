angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Pilih operasi: +, -, *, /")
operator = input("Operator: ")

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    hasil = "Operator tidak dikenal"

print(f"Hasil: {hasil}")


"""
Latihan di rumah:
Modifikasi koding diatas:
- Tambahkan operasi **
- Kasih peringatan kalau pembagian nol
"""