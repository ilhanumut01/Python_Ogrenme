def faktoriyel(sayi):
    if(sayi == 0):
        return 1
    else:
        return sayi * faktoriyel(sayi - 1)
 


kullanici_sayi = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz: "))
print(faktoriyel(kullanici_sayi))
