from geometri.segitiga import Segitiga
from geometri.persegi_panjang import PersegiPanjang
from geometri.bangun_ruang import BangunRuang

print("Menggunakan OOP")
p1 = PersegiPanjang(11,7)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(11, 7)
print(s1.info())
print(s1.hitung_luas())

print("Membuat Object dari kelas BangunRuang")
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

#Polymorphism: kemampuan object untuk merespon berbeda, terhadap pemanggilan methode yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print("Polymorphism")
for n in daftar_bangun_ruang:
    print(n.info())