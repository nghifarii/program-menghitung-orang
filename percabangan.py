# Contoh 1

lulus = raw_input("Apakah kamu lulus? [ya/tidak]")

if lulus == "ya":
  print ("Selamat anda lulus")
else:
  print ("Kamu harus remedial")
  
  
# Contoh 2

# progran mengecek bonus dan diskon

total_belanja = input ("total belanja: Rp ")

# jumlah yang harus dibayar adalah berapa total belanjaannya
# tapi kalau dapat diskon akan berkurang

bayar = total_belanja

# jika dia belanja di atas 100rb maka berikan bonus dan diskon
if total_belanja > 100000:
  print ("kamu mendapatkan bonus minuman dingin")
  print ("dan diskon 5% ")
  
  # hitung diskonnya
  diskon = total_belanja * 5/100 # 5%
  bayar = total_belanja - diskon
 

#cetak struk
print ("Total yang harus dibayar: Rp %s" % bayar)
print ("Terima kasih sudah berbelanja ")
print ("Datang lagi yaa")

