class Flower :
    def __init__(self,nama,jumlah_kelopak,harga):
        self.nama=nama
        self.jumlah_kelopak=jumlah_kelopak
        self.harga=harga

    def set_nama(self,new_nama):
        self.nama=new_nama

    def set_jumlah_kelopak(self,new_jumlah_kelopak):
        self.nama=new_jumlah_kelopak
        
    def harga(self,new_harga):
        self.nama=new_harga


flower1=Flower("Melati",5,2000)
print("Bunga ",flower1.nama, "berkelopak ", flower1.jumlah_kelopak, " harganya ", flower1.harga)
flower1.set_nama("Mawar")
print("Bunga ",flower1.nama, "berkelopak ", flower1.jumlah_kelopak, " harganya ", flower1.harga)