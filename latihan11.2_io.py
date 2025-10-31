'''buah = ("apel", "jeruk", "mangga")

print("ini tuple buah", buah)
print("buah kesatu", buah[0])
print("jumlah buah", len(buah))'''

#praktik 2
'''tuple_campuran = ("Andi", 20, True, 3.14)
print("tuple campuran", tuple_campuran)'''

#praktik 3
#Nested tuple
'''hewan_favorit = ("surya", "adit", ("dower", "lana"))
print("\ntuple bersarang: ", hewan_favorit)
print("\nakses hewan tertentu: ", hewan_favorit[1])
print("\nakses hewan tertentu: ", hewan_favorit[2][1])'''


#praktik 4
'''HariDalamMinggu = ("senin", "selasa", "rabu", "kamis" ,"jumat", "sabtu", "minggu")'''

#input data  pribadi
nama = input("masukan nama lengkap: ")
umur = int(input("masukan umur: "))
alamat = input("masukan Alamat: ")
tinggi = float(input("masukan tinggi badan: "))
nilai = int(input("masukan nilai anda: "))

#proses
tahun_lahir = 2025 - umur
#penentuan nilai
if nilai >= 70:
    keterangan="lulus"
else: "gagal"

#cetak
print("---biodata anda---"
      "\nNama\t\t: %s"
      "\numur\t\t: %i tahun"
      "\nalamat\t\t: %s"
      "\ntinggi badan\t: %.1f cm"
      "\ntahun lahir\t: %i"
      "\nnilai\t\t: %i"
      "\nketerangan\t: %s"
      %(nama, umur, alamat, tinggi, tahun_lahir, nilai, keterangan)
      )
print("\n")
