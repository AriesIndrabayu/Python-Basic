# konstanta nama file, biar gampang diubah
CATATAN_FILE = "catatan.txt"


def tulis_catatan():
    """Fungsi untuk menulis catatan"""
    catatan = input("Tulis catatanmu: ").strip()

    # Validasi input catatan agar tidak kosong
    if not catatan:
        print("Catatan tidak boleh kosong!\n")
        return

    try:
        """
        - perlu ditambahkan encoding="utf-8" untuk antisifasi karakter non-ASCII
        """
        with open(CATATAN_FILE, "a") as file:
            file.write(catatan + "\n")
        print("Catatan berhasil disimpan.\n")
    except Exception as e:
        print(f"Terjadi error saat menyimpan catatan: {e}\n")


def baca_catatan():
    """Fungsi untuk membaca isi catatan"""
    try:
        """
        - perlu ditambahkan encoding="utf-8" untuk antisifasi karakter non-ASCII
        - perlu ditambahkan nomor pada tiap-tiap barisnya supaya lebih rapi
        """
        with open(CATATAN_FILE, "r") as file:
            isi = file.read().strip()
            if isi:
                print("\n=== Isi Catatan Harian ===")
                print(isi)
            else:
                print("\nCatatan masih kosong.\n")
    except FileNotFoundError:
        print("\nBelum ada catatan. Yuk, tulis dulu!\n")
    except Exception as e:
        print(f"Terjadi error saat membaca catatan: {e}")


def tampilkan_menu():
    """Fungsi untuk menampilkan menu"""
    print("=== Menu Catatan Harian ===")
    print("1. Tulis Catatan")
    print("2. Baca Catatan")
    print("3. Keluar")


def main():
    """Fungsi utama program, artinya seluruh alur program akan dijalankan disini."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3): ")

        """
        perlu pemisahan logika pemrosesan pilihan menu ke fungsi proses_pilihan agar mudah di skalabilitas
        """

        if pilihan == "1":
            tulis_catatan()
        elif pilihan == "2":
            baca_catatan()
        elif pilihan == "3":
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid.\n")


# Jalankan Program
if __name__ == "__main__":
    main()
