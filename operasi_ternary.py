# operasi ternary ini di kenal dengan operator kondisi, karena digunakan untuk
# membuat sebauh ekspresi kondisi seperti percabangan IF/ELSE

# RUMUSNYA <Nilai True> if kondisi else <Nilai False>

#contoh 1
umur = input("Berapa umru kamu? ")
aku = "Bocah" if umur < 10 else "dewasa"

print aku


# contoh 2

jomblo = True
status = ("Menikah", "singel") [jomblo]
print status

