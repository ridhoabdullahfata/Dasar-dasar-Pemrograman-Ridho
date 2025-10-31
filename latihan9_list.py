buah2an = ['pepaya','mangga','pisang','jambu','belimbing']

buah2an [2] = 'apel'
print('buah index 2' ,buah2an[2])
del buah2an[4]
#print('buah index 4',buah2an[4])

buah2an.insert(1,'naga')
buah2an.append('duren')
print("----cetak all data----")
for buah in buah2an:
      print("buah", buah)
      
print("potong list",buah2an[1:5])