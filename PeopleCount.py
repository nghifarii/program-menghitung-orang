# program-menghitung-orang
class Orang:
  #variabel class, untuk menghitung jumlah orang
  total_orang = 0
  
  def __init__(self, name):
    self.name = name 
    Orang.total_orang += 1
   
  def __del__(self):
    #kurangi total orang jika objek di hapus
    orang.total_orang -= 1
  
  def katakanHalo(self):
    print ("Halo, nama saya %s, apa kabar? " % self.nama)
  
  def total_populasi(self):
    print ("total orang %s " cls.total)
  
  #method class
  total_populasi = classmethod(total_populasi)
    
org = Orang ("Bubu")
org.katakanHalo()
Orang.total_pupolasi

org2 = Orang("Dede")
org2.katakanHelo()
Orang.total_populasi

print ("objek dihapus, sekarang tinggal ")
del org
del org2

Orang.total_populasi()
