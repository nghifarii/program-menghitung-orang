# Python
"Nomor di setiap hewan"
from enum import Enumenum 
class AnimalEnum(Enum):
    "==========Selamat datang di Penomoran Terhadap Hewan================"
    Kuda = 1
    Sapi = 2
    Ayam = 3
    Kelinci = 4
print (AnimalEnum.__doc__)
print (AnimalEnum.Ayam)
print (repr(AnimalEnum.Ayam))
print("\n")
print (AnimalEnum.Sapi)
print (repr(AnimalEnum.Sapi))
print("\n")
print AnimalEnum.Ayam.name
print ("Ayam dengan nomor " + str(AnimalEnum.Ayam.value))
print("\n")
print AnimalEnum.Sapi.name
print ("Sapi dengan nomor " + str(AnimalEnum.Sapi.value))
print("\n")
for animal in AnimalEnum:
    print ("Name: {}Value: {}". format(animal, animal.value))


""""
Disini kita membuat sebuah Enumeration class dengan nama AnimalEnum.
di dalam class, kita membuat class attributes dengan nama-nama member enumeration, yang konstan.
ketika kamu mencoba untuk print out sebuah member, kamu hanya akan mendapatkan kembali string. 
tapi jika kamu print out the repr dari enum member, kamu akan mendapatkan enum member dan nilainya.
"""
