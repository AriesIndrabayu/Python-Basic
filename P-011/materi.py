# A. File Handling.
"""
r --> baca file
w --> tulis file
a --> nambahin isi ke akhir file (append)
"""
# Menulis ke file
# with open("data.txt", "w") as file:
#     file.write("Halo, ini baris pertama!\n")
#     file.write("Belajar Python itu seru.\n")

# Membaca isi file
# with open("data.txt", "r") as file:
#     isi = file.read()
#     print(isi)


# B. Error Handling: try - except - finally
# Konsep Dasar:
# try:
#     file = open("data.txt", "r")
#     isi = file.read()
#     print(isi)
# except FileNotFoundError:
#     print("File tidak ditemukan.")
# finally:
#     try:
#         file.close()
#         print("File ditutup")
#     except:
#         print("File belum sempat dibuka, jadi tidak perlu ditutup")


# Optimasi dengan with + Error Handling
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File tidak ada, buat dulu filenya.")
