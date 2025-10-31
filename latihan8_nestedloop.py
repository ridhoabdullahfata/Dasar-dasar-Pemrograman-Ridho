#nested looping
print("*")
print("**")
print("***")
print("****")
print("*****")

for i in range(5):
      for j in range(i+1):
          print('*' ,end= ' ')
      print(' ')