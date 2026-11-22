numaralar = [ 84, 57, 92, 27, 111 ]
ogrenciler = ["Ali", "Ayşe", "Kaan", "Osman", "Veli"]

index = 0
for no in numaralar:
    if(no == 92):
        break
    index = index + 1
print(ogrenciler[index]) 


for ogrenci in ogrenciler:
    if (ogrenci == "Osman"):
        continue
    print(ogrenci)

"""
for i in range(len(numaralar)):
    if i == 2:
     for j in range(len(ogrenciler)):
         if j == i:
             print(ogrenciler[j]) """ 

"""             
for i in range(len(ogrenciler)):
    if i == 3:
        continue
    print(ogrenciler[i])"""

