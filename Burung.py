from Animal import * 

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t\t\t\t : ", self.jenis,
        "\nBunyi \t\t\t\t\t : ",  self.bunyi)

anaconda = Burung("Gereja", "Nasi", "Lenteng Agung", "Bertelur", "Batik Solo", "klutuklutuk")
anaconda.cetak_burung()