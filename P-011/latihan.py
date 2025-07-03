def tulis_catatan():
    catatan = input("Tulis catatanmu: ")
    with open("catatan.txt", "a") as file:
        file.write(catatan + "\n")
    print("Catatan berhasil disimpan.\n")


def baca_catatan():
    try:
        with open("catatan.txt", "r") as file:
            print("\n=== Isi Catatan Harian ===")
            print(file.read())
    except FileNotFoundError:
        print("\nBelum ada catatan. Yuk, tulis dulu!\n")


while True:
    print("=== Menu Catatan Harian ===")
    print("1. Tulis Catatan")
    print("2. Baca Catatan")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tulis_catatan()
    elif pilihan == "2":
        baca_catatan()
    elif pilihan == "3":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid.\n")
