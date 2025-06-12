'''
🎯 Tugasnya: Konversi Nilai ke Huruf
- Input: nilai angka 0–100
- Output: huruf A, B, C, D, atau E
- A: ≥ 90
- B: ≥ 80
- C: ≥ 70
- D: ≥ 60
- E: di bawah 60

Tapi, tambahkan juga validasi input!
 ✔ Harus angka
 ✔ Nilai hanya antara 0–100
'''

# Solusi:
nilai = input("Masukkan nilai (0–100): ")

if nilai.isdigit():
    nilai = int(nilai)
    if 0 <= nilai <= 100:
        if nilai >= 90:
            print("A")
        elif nilai >= 80:
            print("B")
        elif nilai >= 70:
            print("C")
        elif nilai >= 60:
            print("D")
        else:
            print("E")
    else:
        print("Nilai harus di antara 0 dan 100!")
else:
    print("Input harus berupa angka!")
