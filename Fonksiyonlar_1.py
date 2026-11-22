"""
def karesini_hesapla(sayi):
    return sayi**2

karesi_alinacak_sayi = int(input("Karesi alınacak sayıyı giriniz: "))
print("Sayının karesi:", karesini_hesapla(karesi_alinacak_sayi))
"""
"""
def isim_ve_yas(isim,yas):
    print("İsim:",isim," Yaş:",yas)
    
    
isim_ve_yas("Umut", 22)
"""

def cift_mi_tek_mi(sayi):
     if(sayi % 2 ==0):
      print("Girilen sayı çifttir.")
     else:
         print("Girilen sayı tektir.")
         

alinacak_sayi = int(input("Bir sayı giriniz:"))         
cift_mi_tek_mi(alinacak_sayi)   
        