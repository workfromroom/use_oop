class KelilingSegitiga:

    def __init__(self,sisi):
        #fungsi yang pertama kali saat object diciptakan
        self.sisi = sisi

    def info(self):
        print("Package untuk menghitung keliling segitiga")

    def hitung_keliling(self):
        return self.sisi + self.sisi + self.sisi
