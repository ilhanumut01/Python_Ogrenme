
islem_durumu = ""

def bolme_fonksiyonu(bolunen,bolen):
    try:
     bolum = bolunen / bolen
     global islem_durumu
     islem_durumu = "başarılı"
     return bolum
    except ZeroDivisionError:    
        islem_durumu = "başarısız"
        print("Hatalı veri girişi var -sıfırla bölme hatası - bölme işlemi yapılamıyor !!!")
    except:
        islem_durumu = "başarısız"
        print("lütfen rakam giriniz, harf girmeyiniz")
    finally:
        print("fonksiyon çalışma sonucu: ", islem_durumu)

print(bolme_fonksiyonu(12,0))

print("Hoşçakalın")
