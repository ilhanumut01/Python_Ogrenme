class Otomobil():
    klima = "klima yok"
    teker_sayisi = 4
    
    def __init__(self, marka, model, yil, km):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.km = km

# Otomobil audi_oto = new Otomobil("Audi", "A3", 2017, 18000);   // Java 
audi_oto = Otomobil("Audi", "A3", 2017, 18000)
opel_oto = Otomobil("Opel", "Astra", 2015, 27000)     
sahin_oto = Otomobil("Tofaş", "Şahin", 1999, 320000)

audi_oto.klima = "Otomotik klima"
opel_oto.klima = "Manuel klima"

print(audi_oto.marka, "", audi_oto.model, "", audi_oto.yil, "", audi_oto.km, "", audi_oto.klima)
print(opel_oto.marka, "", opel_oto.model, "", opel_oto.yil, "", opel_oto.km, "", opel_oto.klima)
print(sahin_oto.marka, "", sahin_oto.model, "", sahin_oto.yil, "", sahin_oto.km, "", sahin_oto.klima)

satilik_arac_list = [audi_oto, opel_oto, sahin_oto]

# for i in satilik_arac_list:
#    print(i.marka, i.model, i.yil, i.km)