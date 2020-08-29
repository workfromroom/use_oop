from geometri.bangun_ruang import BangunRuang

class PersegiPanjang(BangunRuang):
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
    def info(self):
        return f"Ini adalah object dari Persegi Panjang dengan panjang={self.panjang} dan lebar={self.lebar}"
    def hitung_luas(self):
        return self.panjang * self.lebar
