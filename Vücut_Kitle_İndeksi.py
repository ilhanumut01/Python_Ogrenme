#Vücut kitle indekis hesaplama

boy = float(input("Boyunuzu giriniz(metre cinsinden):"))
kilo = float(input("Kilonuzu giriniz(kg cinsiden):"))

beden_kitle_indeksi = kilo / (boy**2)
print(beden_kitle_indeksi)

if(beden_kitle_indeksi < 18.5):
    print("Zayıf")
elif(18.5 <= beden_kitle_indeksi <= 25):
    print("Normal")
elif(25 < beden_kitle_indeksi < 30):
        print("Kilolu")
elif(beden_kitle_indeksi >= 30):
        print("Obez")
    