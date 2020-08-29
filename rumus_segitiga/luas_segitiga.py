class LuasSegitiga():

    def __init__(self,alas,tinggi):
        #fungsi yang pertama kali saat object diciptakan
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        print("Ini adalah object dari segitiga dengan alas=",{self.alas},"dan tinggi=",{self.tinggi})

    def hitung_luas(self):
        return self.alas * self.tinggi / 2