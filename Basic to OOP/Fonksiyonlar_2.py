"""
def ekrana_yazdir(bilgi):
    print(bilgi)
    
       
def kare_hesapla(sayi):
   sayinin_karesi = sayi * sayi
   ekrana_yazdir(sayinin_karesi)

kare_hesapla(12)
kare_hesapla(15)
"""

def kare_kup_hesapla(sayi):
    kare = sayi * sayi
    kup = sayi * sayi * sayi
    return kare , kup

sayi = 3
sayinin_karesi , sayinin_kupu = kare_kup_hesapla(sayi)
print("Sayının karesi:",sayinin_karesi,"Sayının kupu:",sayinin_kupu)