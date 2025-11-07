nilai = { 'Harno':89, 'Jayadi':100, 'Kholik':59,'Jawir':95}
print("Data nilai : " ,nilai)

print("\n------------cetak valuenya saja---------------------\n")
#cetak nilai saja
for skor in nilai.values():
    print("Data Nilai : " ,skor)
    
    print("\n------------cetak key aja---------------------\n")
#cetak nama saja
for nama in nilai.keys():
    print("Data Siswa : " ,nama)
    
#cetak nama dan nilai
print("\n------------cetak key dan valuenya---------------------\n")
for nama ,skor in nilai.items():
    print("Data Siswa dan Nilai : " ,nama ,"Memiliki nilai" ,skor)

#mengubah nilai di dictionary
nilai['Kholik'] = 75
print ("Data Nilai Kholik Setelah diubah : " ,nilai['Kholik'])

#mengapus item di dictionary
del nilai['Jawir']
print("\nData nilai setelah dihapus Jawir : " ,nilai)