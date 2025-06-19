nilai = [80, 85, 78, 90]
rata2 = sum(nilai) / len(nilai)

# Tentukan predikat
if rata2 >= 90:
    predikat = "A (Sangat Baik)"
elif rata2 >= 80:
    predikat = "B (Baik)"
elif rata2 >= 70:
    predikat = "C (Cukup)"
else:
    predikat = "D (Perlu Perbaikan)"

print("Rata-rata:", rata2)
print("Predikat:", predikat)
