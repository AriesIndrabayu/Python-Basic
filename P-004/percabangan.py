# struktur if dan else
umur = 20
if umur >= 18:
    print("Dewasa")
else:
    print("Belum Dewasa")
    
# Struktur if, elif dan else
nilai = 85
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
else:
    print("C atau di bawahnya")
    
'''
Contoh Kasus:
Bayangin kamu lagi nonton YouTube:
- Kalau sinyal bagus → 1080p
- Kalau agak lelet → 720p
- Kalau pas-pasan banget → 360p

Itu kayak gini kalau ditulis di Python:

'''
kecepatan = 3
if kecepatan >= 10:
    print("1080p")
elif kecepatan >= 5:
    print("720p")
else:
    print("360p")
