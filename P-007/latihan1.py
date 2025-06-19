belanja = [
    ("Mie Instan", 3000),
    ("Minyak Goreng", 20000),
    ("Sabun Mandi", 10000)
]

total = 0
for item in belanja:
    print(f"- {item[0]}: Rp {item[1]}")
    total += item[1]

print("Total:", total)

# Percabangan
if total < 50000:
    print("Kategori: Belanja irit!")
elif total <= 100000:
    print("Kategori: Cukup lah!")
else:
    print("Kategori: Wah, boros juga 😅")
