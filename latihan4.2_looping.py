print ("Menghitung Total Belanja")
jml_barang = int (input("Masukkan jumlah barang"))
total = 0

for i in range (1, jml_barang + 1):
     harga = int(input(f"Masukkan harga             barang ke-{i}: ")) 
     total += harga
     
print(f"total belanja anda adalah:         Rp:{total}")

pw = "python123"
percobaan = 1

while percobaan <= 3:
    password = input("Masukkan                        password:")
    if password == pw:
         print("Login berhasil")
         break
    else:
        print("Password salah,silahkan                     coba lagi./n")
        percobaan +=1
           
if percobaan > 3:
    print("Akses ditolak! karna melebihi             batas percobaan")
    
    
print("TABEL PERKALIAN")
n = int(input("Tampilkan tabel perkalian             sampai angka: "))

for i in range(1, n + 1):
    for j in range (1, n + 1):
          print (f"{i*j:3}", end=" ")
        
    print()
             
a = 5


for i in range(a, 0, -1):
    for j in range(a - i):
         print(' ', end=' ')
        
    
    for j in range(0, i + 1):
        print('*  ', end=' ')
    print()