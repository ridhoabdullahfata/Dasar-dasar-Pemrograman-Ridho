'''nama = input("Nama siswa\t: ")
matpel = str(input("Mata pelajaran\t: "))
nilai = float(input("Nilai siswa\t: "))
#tuple & list
ket = ("Gagal", "Lulus")[nilai >= 60]
#cetak dengan format print
print("-----Data Niai Siswa-----"
    "\nNama siswa\t: %s"
    "\nMata pelajaran\t: %s"
    "\nNilai siswa\t:%.2f"
    "\nKeterangan\t: %s"
    %(nama, matpel, nilai, ket)
)'''

nama = (input("Nama siswa\t :"))
juamlah_uang = float(input("jumlah uang\t: "))
ket = ("uang tidak cukup", "uang cukup")[juamlah_uang >= 1000]

print("-----tabungan siswa-----"
      "\nnama siswa\t: %s"
      "\njumlah uang siswa\t\t: %.2f"
      "\nalamat\t: %s"
      %(nama, juamlah_uang, ket)
      )

