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
        with open(
            CATATAN_FILE, "a", encoding="utf-8"
        ) as file:  # encoding="utf-8" untuk antisifasi karakter non-ASCII
            file.write(catatan + "\n")
        print("Catatan berhasil disimpan.\n")
    except Exception as e:
        print(f"Terjadi error saat menyimpan catatan: {e}\n")


def baca_catatan():
    """Fungsi untuk membaca isi catatan"""
    try:
        with open(
            CATATAN_FILE, "r", encoding="utf-8"
        ) as file:  # encoding="utf-8" untuk antisifasi karakter non-ASCII
            # penomoran pada catatan ketika ditampilkan
            baris_catatan = (
                file.readlines()
            )  # membuat list dimana setiap elemennya adalah satu baris dari file tersebut

            if baris_catatan:
                print("\n=== Isi Catatan Harian ===")
                for index, baris in enumerate(baris_catatan, start=1):
                    print(f"{index}. {baris.strip()}")
                print()  # Baris kosong setelah catatan
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


def proses_pilihan(pilihan):
    """Fungsi untuk memproses pilihan menu. Dipisah agar mudah dikembangkan kedepannya"""
    if pilihan == "1":
        tulis_catatan()
    elif pilihan == "2":
        baca_catatan()
    elif pilihan == "3":
        print("Terima kasih! Sampai jumpa.")
        return False  # menghentikan loop pada fungsi main
    else:
        print("Pilihan tidak valid.\n")
    return True  # melanjutkan looop di fungsi main


def main():
    """Fungsi utama program, artinya seluruh alur program akan dijalankan disini."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if not proses_pilihan(pilihan):
            break


# Jalankan Program
if __name__ == "__main__":
    main()


"""
- Konfirmasi sebelum keluar (y/n)
- belum ada fitur hapus semua catatan
- belum ada fitur hapus catatan tertentu berdasarkan nomornya
"""
