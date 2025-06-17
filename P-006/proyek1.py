# Game tebak angka
import random

angka_rahasia = random.randint(1, 20)
max_tebakan = 5
print("Selamat datang di permainan Tebak Angka!")
print("Saya telah memilih angka antara 1 sampai 20.")

for percobaan in range(1, max_tebakan + 1):
    tebakan = int(input(f"Tebakan ke-{percobaan}: "))
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"Selamat! Kamu menebak dengan benar di percobaan ke-{percobaan}.")
        break
else:
    print(f"Maaf, kamu gagal menebak. Angka yang benar adalah {angka_rahasia}.")
