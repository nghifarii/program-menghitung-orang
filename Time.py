# Python
import time
print ("Apakah anda mau meluncurkan roket?\n")
raw_input("Tekan [Enter] untuk memulai...")

for i in range(10, 0, -1):
    time.sleep(0.5)
    print ("Berhitung: " + str(i))
if i == 1:
    time.sleep(2)
    print ("Buzzzzz....!!!!")
    time.sleep(1)
    print ("Roket telah meluncur.")
