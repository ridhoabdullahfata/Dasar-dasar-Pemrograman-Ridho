#latihan 1
nilai = 80
if nilai >= 75:
  print("LULUS")
else:
   print("TIDAK LULUS")
   
#latihan2
# nilai = 70
nilai = int(input("masukkan nilai: "))
if nilai >=90:
   print  ("Nilai kamu: A")
elif nilai >=80:
    print ("Nilai kamu: B")
elif nilai >=70:
    print ("Nilai kamu: C")
else:
   print ("Nilai kamu: E")
   
 # IF ternary
nilai = 80
status = "lulus" if nilai >= 75 else "tidak lulus"
print("status anda",status)
   
#latihan modulus
angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    print ("Angka",angka,"adalah genap")
else:
    print("Angka",angka,"adalah ganjil")
