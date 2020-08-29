class KelilingSegitiga():

    def __init__(self,sisi):
        #fungsi yang pertama kali saat object diciptakan
        self.sisi = sisi

    def info(self):
        return f"Ini adalah object dari segitiga dengan sisi={self.sisi}"

    def hitung_keliling(self):
        return self.sisi + self.sisi + self.sisi
