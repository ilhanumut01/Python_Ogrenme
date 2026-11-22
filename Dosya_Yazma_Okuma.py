import os

# print(os.listdir()) Bu dosya dizinin altındaki dosyaları çeker  

# Metin dosyası oluşturma
ogrenci_dosya = os.open("ogrenciler.txt", os.O_RDWR|os.O_CREAT)

# ogrenciler.txt dosyasına öğrenci ismi ve sınav notu yazdıralım
os.write(ogrenci_dosya, "Ali Er, 70\n".encode())
os.write(ogrenci_dosya, "Mehmet Kaya, 50\n".encode())
os.write(ogrenci_dosya, "Ayşe Su, 100\n".encode())
os.write(ogrenci_dosya, "Nihan Korkmaz, 90\n".encode())

os.close(ogrenci_dosya)

# ogrenciler.txt dosyasındaki metni okuma
ogrenci_dosya = os.open("ogrenciler.txt", os.O_RDONLY)
dosya_uzunluk = os.stat(ogrenci_dosya).st_size
icerik = os.read(ogrenci_dosya, dosya_uzunluk)
print(icerik.decode())

os.close(ogrenci_dosya)
"""
# Dosyayı silme
os.unlink("ogrenciler.txt")
"""