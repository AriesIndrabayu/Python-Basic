# Variabel dengan tipe data string
nama = "Bayu"
# Variabel dengan tipe data integer
umur = 20
# Variabel dengan tipe data float
tinggi = 165.5

nama = 12 # Ini sih gak error, tapi sangat tidak disarankan!
print("\nData Ke-1: ")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)

"""_summary_
Tips Pentng:
Kalo kita pengen jaga data lebih ketat, nanti di Python bisa pakai type hint. Contoh...
"""
print("\nData Ke-2: ")

namaku: str = "Dudung"
namaku = 123
umur: int = 45
tinggi = 170

print("Nama:", namaku)
print("Umur:", umur)
print("Tinggi:", tinggi)

