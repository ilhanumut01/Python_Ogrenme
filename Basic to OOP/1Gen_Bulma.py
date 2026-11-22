import random
import time

# ---- ZAMAN ÖLÇÜMÜNÜ BAŞLAT ----
baslangic_zamani = time.time()

def genetik_dizi_olustur(uzunluk):
    """Belirtilen uzunlukta rastgele bir genetik dizi oluşturur."""
    bazlar = ['A', 'T', 'G', 'C']
    return "".join(random.choice(bazlar) for _ in range(uzunluk))

# Aranacak olan spesifik dizilim
aranan_dizilim = "ACTAGATG"

# 150.000.000 elemanlı rastgele bir genetik dizi oluşturuluyor
ornek_dizi_uzunlugu = 200000000
ornek_genetik_dizi = genetik_dizi_olustur(ornek_dizi_uzunlugu)

# Oluşturulan dizi içinde aranan dizilimin kaç tane olduğu sayılıyor
bulunan_sayisi = ornek_genetik_dizi.count(aranan_dizilim)

# ---- ZAMAN ÖLÇÜMÜNÜ BİTİR ----
bitis_zamani = time.time()

# Geçen süreyi hesapla
gecen_sure = bitis_zamani - baslangic_zamani

# Sonuçlar ekrana yazdırılıyor
print(f"Olusturulan Ornek Genetik Dizinin Uzunlugu: {ornek_dizi_uzunlugu}")
print("-" * 40)
print(f"Aranan Dizilim: '{aranan_dizilim}'")
print(f"'{aranan_dizilim}' dizilimi, ornek dizi icinde {bulunan_sayisi} kez bulundu.")
print("-" * 40)
print("Yuzde",bulunan_sayisi/1500000,"'dir")
print(f"Islem toplam {gecen_sure:.4f} saniye surdu.")