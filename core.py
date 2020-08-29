from rumus_segitiga.luas_segitiga import LuasSegitiga
from rumus_segitiga.keliling_segitiga import KelilingSegitiga

print("Belajar Menggunakan OOP")
print("-" * 59)

l = LuasSegitiga(11,9)
print(l.info())
print("Luas Segitiga adalah",l.hitung_luas())

print()

s = KelilingSegitiga(11)
print(s.info())
print("Keliling Segitiga adalah",s.hitung_keliling())