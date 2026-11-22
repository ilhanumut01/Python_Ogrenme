import os

# ogrenciler.txt dosyasındaki metni okuma
ogrenci_dosya = os.open("ogrenciler.txt", os.O_RDONLY)
dosya_uzunluk = os.stat(ogrenci_dosya).st_size
icerik = os.read(ogrenci_dosya, dosya_uzunluk)

ogrenciler = icerik.decode()

ogrenciler_list = ogrenciler.split("\n")

# print(ogrenciler_list)

ogrenci_sayisi = len(ogrenciler_list)-1
# print(ogrenci_sayisi)

index = 0
toplamlar_notlar = 0
while index < ogrenci_sayisi:
#   print(ogrenciler_list[index])
    ogrenci_notu = ogrenciler_list[index].split(",")
    toplamlar_notlar += int(ogrenci_notu[1])
    index += 1
print("Sınav notlarının ortlaması:",toplamlar_notlar/ogrenci_sayisi)

os.close(ogrenci_dosya)