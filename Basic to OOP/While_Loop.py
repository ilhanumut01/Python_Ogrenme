
# faktöriyel hesabı

def faktoriyel(sayi):
        sonuc = 1
        while(sayi > 0):
            sonuc = sonuc * sayi
            sayi = sayi - 1   
        return sonuc      
                      
x = int(input("Faktöriyeli alınacak sayıyı giriniz:"))

print(faktoriyel(x))  

"""
mesaj = input("Mesaj yazın: ")
while (mesaj != "kapat"):
    print(mesaj)
    mesaj = input("Bir şey yaz: ") """
