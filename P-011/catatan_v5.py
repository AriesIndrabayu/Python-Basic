import shutil
import datetime
import os

# konstanta nama file, biar gampang diubah
CATATAN_FILE = "catatan.txt"
BACKUP_FOLDER = "backup"


def buat_backup():
    """Fungsi untuk membuat backup otomatis sebelum penghapusan"""
    try:
        nama_backup = f"{BACKUP_FOLDER}/backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        shutil.copy(CATATAN_FILE, nama_backup)
        print(f"✅ Backup berhasil dibuat: {nama_backup}\n")
    except FileNotFoundError:
        print("ℹ Tidak ada file yang dibackup karena catatan belum ada.\n")
    except Exception as e:
        print(f"❌ Gagal membuat backup: {e}\n")


def tulis_catatan():
    """Fungsi untuk menulis catatan"""
    catatan = input("Tulis catatanmu: ").strip()

    # Validasi input catatan agar tidak kosong
    if not catatan:
        print("⚠ Catatan tidak boleh kosong!\n")
        return

    try:
        with open(
            CATATAN_FILE, "a", encoding="utf-8"
        ) as file:  # encoding="utf-8" untuk antisifasi karakter non-ASCII
            file.write(catatan + "\n")
        print("✅ Catatan berhasil disimpan.\n")
    except Exception as e:
        print(f"❌ Terjadi error saat menyimpan catatan: {e}\n")


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
                print("\nℹ Catatan masih kosong.\n")
    except FileNotFoundError:
        print("\nℹ Belum ada catatan. Yuk, tulis dulu!\n")
    except Exception as e:
        print(f"❌ Terjadi error saat membaca catatan: {e}")


def hapus_semua_catatan():
    """Fungsi untuk menghapus seluruh isi catatan"""

    try:
        with open(CATATAN_FILE, "r", encoding="utf-8") as file:
            baris_catatan = file.readlines()
        if not baris_catatan:
            print("\nℹ Tidak ada catatan yang bisa dihapus.\n")
            return

        konfirmasi = (
            input("Yakin ingin menghapus semua catatan? (y/n): ").strip().lower()
        )
        if konfirmasi == "y":
            buat_backup()  # panggil fungsi backup
            try:
                with open(CATATAN_FILE, "w", encoding="utf-8"):
                    pass  # kosongkan isi file
                print(f"✅ Semua catatan berhasil dihapus.\n")
            except Exception as e:
                print(f"❌ Terjadi kesalahan saat menghapus catatan: {e}\n")
        else:
            print("ℹ Penghapusan dibatalkan.\n")
    except FileNotFoundError:
        print("\nℹ Belum ada catatan. Yuk, tulis dulu!\n")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}\n")


def hapus_catatan_tertentu():
    """Fungsi untuk menghapus catatan berdasarkan nomor"""
    try:
        with open(CATATAN_FILE, "r", encoding="utf-8") as file:
            baris_catatan = file.readlines()

        if not baris_catatan:
            print("\nℹ Tidak ada catatan yang bisa dihapus.\n")
            return
        baca_catatan()
        try:
            nomor = int(input("Masukkan nomor catatan yang ingin dihapus: "))
            # memastikan nomor tidak kurang dari 1 dan tidak lebih dari jumlah baris catatan
            if 1 <= nomor <= len(baris_catatan):
                buat_backup()  # penggil fungsi backup
                catatan_terhapus = baris_catatan.pop(nomor - 1)
                with open(CATATAN_FILE, "w", encoding="utf-8") as file:
                    file.writelines(baris_catatan)
                print(f"✅ Catatan '{catatan_terhapus.strip()}' berhasil di hapus.\n")
            else:
                print("⚠ Nomor tidak valid.\n")
        except ValueError:
            print("Input harus berupa angka.\n")
    except FileNotFoundError:
        print("\nℹ Belum ada catatan. Yuk, tulis dulu!\n")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}\n")


def edit_catatan_tertentu():
    """Fungsi untuk mengedit isi catatan berdasarkan nomornya"""
    try:
        with open(CATATAN_FILE, "r", encoding="utf-8") as file:
            baris_catatan = file.readlines()
        if not baris_catatan:
            print("\nℹ Tidak ada catatan yang bisa diedit.\n")
            return

        baca_catatan()
        try:
            nomor = int(input("Masukkan nomor catatan yang ingin di edit: "))
            if 1 <= nomor <= len(baris_catatan):
                catatan_lama = baris_catatan[nomor - 1].strip()
                print(f"Catatan lama: {catatan_lama}")
                catatan_baru = input("Tuliskan catatan baru: ").strip()
                if not catatan_baru:
                    print("⚠ Catatan baru tidak boleh kosong.\n")
                    return
                buat_backup()
                baris_catatan[nomor - 1] = catatan_baru + "\n"
                with open(CATATAN_FILE, "w", encoding="utf-8") as file:
                    file.writelines(baris_catatan)
                print("✅ Catatan berhasil diperbaharui.\n")
            else:
                print("⚠ Nomor idak valid.\n")
        except ValueError:
            print("⚠ Input harus berupa angka.\n")
    except FileNotFoundError:
        print("\nℹ Belum ada catatan. Yuk, tulis dulu!\n")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}\n")


def export_catatan():
    """Fungsi untuk mengekspor catatan ke file lain"""
    nama_file = input("Masukkan nama file tujuan (contoh: export.txt): ").strip()
    if not nama_file:
        print("⚠ Nama file tidak boleh kosong.\n")
        return
    try:
        shutil.copy(CATATAN_FILE, nama_file)
        print(f"✅ Catatan berhasil diekspor ke '{nama_file}'.\n")
    except FileNotFoundError:
        print("ℹ Belum ada catatan yang bisa diekspor.\n")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat ekspor file: {e}\n")


def cari_catatan():
    """Fungsi untuk mencari kata dalam catatan"""
    kata_kunci = input("Masukkan kata yang ingin di cari: ").strip().lower()
    if not kata_kunci:
        print("⚠ Kata kunci tidak boleh kosong.\n")
        return
    try:
        with open(CATATAN_FILE, "r", encoding="utf-8") as file:
            baris_catatan = file.readlines()
        hasil = []
        for index, baris in enumerate(baris_catatan, start=1):
            if kata_kunci in baris.lower():
                hasil.append(f"{index}. {baris.strip()}")

        if hasil:
            print("\n=== Hasil Pencarian ===")
            for item in hasil:
                print(item)
            print()
        else:
            print(f"ℹ Tidak ditemukan catatan yang mengandung kata '{kata_kunci}'.\n")
    except FileNotFoundError:
        print("\nℹ Belum ada catatan. Yuk, tulis dulu!\n")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat pencarian: {e}\n")


def tampilkan_menu():
    """Fungsi untuk menampilkan menu"""
    print("=== Menu Catatan Harian ===")
    print("1. Tulis Catatan")
    print("2. Baca Catatan")
    print("3. Hapus Catatan Semua")
    print("4. Hapus Catatan Tertentu")
    print("5. Edit Catatan Tertentu")  # penambahan menu
    print("6. Cari Catatan")  # penambahan menu
    print("7. Ekspor Catatan Ke File Lain")  # penambahan menu
    print("8. Keluar")


def proses_pilihan(pilihan):
    """Fungsi untuk memproses pilihan menu. Dipisah agar mudah dikembangkan kedepannya"""
    if pilihan == "1":
        tulis_catatan()
    elif pilihan == "2":
        baca_catatan()
    elif pilihan == "3":
        hapus_semua_catatan()
    elif pilihan == "4":
        hapus_catatan_tertentu()
    elif pilihan == "5":
        edit_catatan_tertentu()
    elif pilihan == "6":
        cari_catatan()
    elif pilihan == "7":
        export_catatan()
    elif pilihan == "8":
        konfirmasi = input("Yakin ingin keluar? (y/n): ").strip().lower()
        if konfirmasi == "y":
            print("👋 Terima kasih! Sampai jumpa.")
            return False  # menghentikan loop pada fungsi main
        else:
            print("ℹ Keluar dibatalkan.\n")
    else:
        print("⚠ Pilihan tidak valid. Silahkan pilih angka 1-8\n")
    return True  # melanjutkan looop di fungsi main


def main():
    """Fungsi utama program, artinya seluruh alur program akan dijalankan disini."""

    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4/5/6/7/8): ").strip()

        # validasi terhadap pilihan menu
        if pilihan not in {"1", "2", "3", "4", "5", "6", "7", "8"}:  # set literal
            print("⚠ Pilihan tidak valid. Silahkan pilih angka 1-8\n")
            continue

        if not proses_pilihan(pilihan):
            break


# Jalankan Program
if __name__ == "__main__":
    main()


"""
- ✅ validasi untuk hapus semua catatan jika kosong
- ✅ export catatan ke file lain
- ✅ pencarian kata dalam catatan
- ✅ backup otomatis catatan sebelum menghapus semua atau tertentu
- ✅ tambahin menu edit catatan
"""
