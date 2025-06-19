# buah = ["semangka", "apel", "jeruk", "pisang"]
# angka = [1, 3, 2, 5, 4]
# buah.sort(reverse=True)
# print(buah)
# buah.reverse() # --> ini di urut berdasarkan indexnya
# print(buah)
# urutBuah = sorted(buah, reverse=True)
# urutTerbalikBuah = list(reversed(buah))

# print(buah)
# print(urutBuah)
# print(urutTerbalikBuah)

'''
| Fungsi           | Efeknya                                   | Return value                   |
| ---------------- | ----------------------------------------- | ------------------------------ |
| `list.sort()`    | Urutkan langsung                          | `None`                         |
| `list.reverse()` | Balik urutan langsung                     | `None`                         |
| `sorted(list)`   | Menghasilkan list baru yang sudah terurut | ✅ list                         |
| `reversed(list)` | Menghasilkan iterator yang dibalik        | ✅ iterator (perlu `list(...)`) |



| Fungsi           | Mengubah List Asli? | Return Value | Contoh Aman                   |
| ---------------- | ------------------- | ------------ | ----------------------------- |
| `buah.reverse()` | ✅ Ya                | ❌ None       | `buah.reverse(); print(buah)` |
| `reversed(buah)` | ❌ Tidak             | ✅ Iterator   | `list(reversed(buah))`        |

'''

# koordinat = (10,20)
# buah = ("apel", "jeruk", "mangga")

# print(koordinat)
# 1. Indexing dan Slicing
# print(koordinat[0])
# print(buah[1:3])

# 2. Penggabungan (Concatenation)
# t1 = (1, 2)
# t2 = (3, 4)
# hasil = t1 + t2
# print(hasil)  # Output: (1, 2, 3, 4)

# 3. Pengulangan (Repetition)t = ("hai",)
# t = ("hai",)
# ulang = t * 3
# print(ulang)  # Output: ('hai', 'hai', 'hai')

# 4. Pengecekan Anggota (in, not in)
# angka = (1, 2, 3)
# print(10 in angka)     # Output: True
# print(5 not in angka) # Output: True

# 5. Looping dengan for
# hewan = ("kucing", "anjing", "kelinci")
# for h in hewan:
#     print(h)

# 6. Fungsi Bawaan: len(), min(), max(), sum()
# angka = (5, 1, 8, 3)
# print(len(angka))  # Output: 4
# print(min(angka))  # Output: 1
# print(max(angka))  # Output: 8
# print(sum(angka))  # Output: 17

# 7. Mengubah Tuple ke List (kalau mau dimodifikasi)
# t = (1, 2, 3)
# l = list(t)
# l.append(4)
# t = tuple(l)
# print(t)  # Output: (1, 2, 3, 4)

# 8. Unpacking Tuple
# person = ("Bayu", 30, "Programmer")
# nama, umur, profesi = person
# print(nama)     # Output: Bayu
# print(umur)     # Output: 30
# print(profesi)  # Output: Programmer

# 🛑 Operasi yang Tidak Bisa:
t = (1, 2, 3)
t[0] = 100  # ❌ Error: 'tuple' object does not support item assignment