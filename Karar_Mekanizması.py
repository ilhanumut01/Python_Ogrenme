# otomobil kredisi hesaplama

kredi_miktari = int(input("Kredi miktarını giriniz:"))
odenecek_total_kredi = 0


if(kredi_miktari >= 100000):
    
    odenecek_total_kredi = odenecek_total_kredi + (kredi_miktari * 1.79)
    print("Ödenecek toplam para:",odenecek_total_kredi)
    
elif(50000 <= kredi_miktari < 100000):
    
    odenecek_total_kredi = odenecek_total_kredi + (kredi_miktari * 1.65)
    print("Ödenecek toplam para:",odenecek_total_kredi)
    
elif(0 <= kredi_miktari < 50000):
    odenecek_total_kredi = odenecek_total_kredi + (kredi_miktari * 1.52)
    print("Ödenecek toplam para:",odenecek_total_kredi)

elif(kredi_miktari < 0):
    print("Yanlış ifade girdiniz!!!")    
    
    
    