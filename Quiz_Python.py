# bir tam sayı listesi içindeki çift sayıları bulan bir fonksiyon yazınız...
liste = [1, 5, 7, 8, 12, 45, 78, 121,2]  # Örnek liste
                                         # Cevabınız : 3 olmalı...


def cift_sayilari_bul(sayilar):
    sayac = 0
    for sayi in sayilar:
        if (sayi % 2) == 0:
            sayac += 1
    return sayac 

def tek_sayilari_bul(sayilar):
    sayac = 0
    for sayi in sayilar:
        if (sayi % 2) == 1:
            sayac += 1
    return sayac      

print("Listedeki çift sayılar:",cift_sayilari_bul(liste))
print("Listedeki tek sayılar:",tek_sayilari_bul(liste))