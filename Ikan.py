from Animal import * 

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_Ikan(self):
        super().cetak()
        print("Jenis \t\t\t\t\t : ", self.jenis,
        "\nBunyi \t\t\t\t\t : ",  self.bunyi)

Lele = Ikan("Lele", "Cacing", "Setu Cilangkap", "Bertelur", "bersisik", "blubukblubuk")
Lele.cetak_Ikan()