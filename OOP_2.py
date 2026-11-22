class Kara_Araci():
    hiz = 0
    def __init__(self, beygir_gucu, teker_sayisi):
        self.beygir_gucu = beygir_gucu
        self.teker_sayisi = teker_sayisi
    
    def hizi_ayarla(self,deger):
        self.hiz = deger
        
class Otobus(Kara_Araci):
    def __init__(self,beygir_gucu,teker_sayisi,yolcu_kapasitesi):
        Kara_Araci.__init__(self, beygir_gucu, teker_sayisi)
        self.yolcu_kapasitesi = yolcu_kapasitesi
    def Tagograg_kontrol(self):
        print("Takograg kontrol edildi")
        
class Otomobil(Kara_Araci):
    def __init__(self, beygir_gucu, teker_sayisi, sunroof):
        Kara_Araci.__init__(self, beygir_gucu, teker_sayisi)
        self.sunroof = sunroof

otobus1 = Otobus(450, 8, 44)
otobus1.hizi_ayarla(80)
otobus1.Tagograg_kontrol()
print("Otobus1 bilgileri:",otobus1.beygir_gucu,"",otobus1.hiz)

otomobil1 = Otomobil(120, 4, "var") 
otomobil1.hizi_ayarla(70)  
 
print("Otomobil1 bilgileri:",otomobil1.beygir_gucu,"",otomobil1.teker_sayisi,"",otomobil1.sunroof) 
print(otomobil1.hiz)