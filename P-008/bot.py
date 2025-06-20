respon = {
    "halo": "Halo juga!",
    "apa kabar": "Saya baik, kamu gimana?",
    "terima kasih": "Sama-sama!",
}

sapaan = {"halo", "hai", "hi"}

user_input = input("Kamu: ").lower()

# Cek sapaan pakai set
if any(kata in user_input for kata in sapaan):
    print("Bot: Hai juga!")
# Cek respon tetap pakai dict
elif user_input in respon:
    print("Bot:", respon[user_input])
else:
    print("Bot: Maaf, saya belum mengerti.")
