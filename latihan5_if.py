pelanggan = "rosied"
produk = "AC"
jumlah = 3
if produk == "AC":
    harga_satuan = 50000
elif  produk == "Kulkas":
    harga_satuan = 40000
elif produk == "Tv":
    harga_satuan = 30000
else:
      harga_satuan = 0
      
bruto = harga_satuan *  jumlah
if produk == "AC" and jumlah >=2:
    diskon = 0.2 * bruto
elif produk == "Kulkas" and jumlah >=2:
    diskon = 0.1 * bruto
else :
     diskon = 0.05 * bruto

ppn = 0.11 * (bruto - diskon)
netto = (bruto - diskon) + ppn

print ("Nama pelanggan\t:",pelanggan,
          "\nproduk\t:",produk,
          "\njumlah\t:",jumlah,
          "\nharga satuan\t:",harga_satuan,
          "\nharga kotor\t:",bruto,
          "\ndiskon\t:",diskon,
          "\nppn\t:",ppn,
          "\njumlah bayar\t:",netto
)
          
          
          
          
         