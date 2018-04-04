# Python
from enum import Enumenum 
class AnimalEnum(Enum):
    Kuda = 1
    Sapi = 2
    Ayam = 3
    Kelinci = 4
print (AnimalEnum.Aya,)
print (repr(AnimalEnum.Ayam))
print (AnimalEnum.Ayam.name)
print (AnimalEnum.ayam.value)

for animal in AnimalEnum:
    print ("Name: {} value: {}".format(animal, animal.value))
    

""""
Disini kita membuat sebuah Enumeration class dengan nama AnimalEnum.
di dalam class, kita membuat class attributes dengan nama-nama member enumeration, yang konstan.
ketika kamu mencoba untuk print out sebuah member, kamu hanya akan mendapatkan kembali string. 
tapi jika kamu print out the repr dari enum member, kamu akan mendapatkan enum member dan nilainya.
"""
