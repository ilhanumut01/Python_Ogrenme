"""
ogrenci_list = ["Ahmet Emre", "Ali Öz", "Veli Can", "Ayşe Su", "Batuhan Emre"]

ogrenci_sayisi = 0
for i in ogrenci_list:
    ogrenci_sayisi = ogrenci_sayisi +1
    print(i)

print(ogrenci_sayisi)  """  

"""
ogrenci_list = ["Ahmet Emre", "Ali Öz", "Veli Can", "Ayşe Su", "Batuhan Emre"]

ogrenci_adi = input("Öğrenci adı-soyadı giriniz:")

if ogrenci_adi in ogrenci_list:
    print("Hoşgeldiniz")
else:
    print("Giriş yetkiniz yok !!!")"""
    
ogrenci_list = ["Ahmet Emre", "Ali Öz", "Veli Can", "Ayşe Su", "Batuhan Emre"]


for i in range(len(ogrenci_list)):    # for(int i = 0;i<lengh(ogrenci_list);i++)
    print(ogrenci_list[i])           # cout << ogrenci_list[i] << endl;