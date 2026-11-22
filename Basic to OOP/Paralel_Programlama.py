import random
import time
import multiprocessing
import numpy as np # Listeyi kolayca bölmek için popüler bir kütüphane

# --- Parametreler ---
Dizi_Sayisi = 1_000_000  # 1 Milyon
Dizi_Uzunlugu = 1000
Aranan_Kelime = "AGTACTCAGT"
# İşlemci çekirdek sayısı
Cekirdek_Sayisi = 8

# --- İşçi Fonksiyonu ---
# Her bir işlemci çekirdeğinin çalıştıracağı fonksiyon budur.
# Kendisine gelen küçük liste parçasında (chunk) arama yapar.
def search_in_chunk(chunk, pattern):
    """Bir liste parçasında belirli bir deseni arar ve eşleşenleri döndürür."""
    matches = []
    for item in chunk:
        if pattern in item:
            matches.append(item)
    return matches

# --- Ana Program Bloğu ---
# Multiprocessing kullanırken ana kodun bu blok içinde olması önemlidir.
if __name__ == "__main__":
    print("="*40)
    print("PARALEL PROGRAMLAMA - GENETİK DİZİ ARAMA SİMÜLASYONU")
    print("="*40)
    print(f"Parametreler:")
    print(f" - Dizi Sayısı: {Dizi_Sayisi:,}")
    print(f" - Dizi Uzunluğu: {Dizi_Uzunlugu}")
    print(f" - Çekirdek Sayısı: {Cekirdek_Sayisi}\n")

    # --- 1. Adım: Veri Oluşturma ---
    print("1 Milyon adet genetik dizi oluşturuluyor...")
    baslangic_zamani_uretme = time.time()
    dizi_listesi = ["".join(random.choices("ACGT", k=Dizi_Uzunlugu)) for _ in range(Dizi_Sayisi)]
    bitis_zamani_uretme = time.time()
    print(f"✔ Veri oluşturma {bitis_zamani_uretme - baslangic_zamani_uretme:.2f} saniyede tamamlandı.\n")

    # --- 2. Adım: Seri Arama (Karşılaştırma için) ---
    print(f"'{Aranan_Kelime}' kelimesi SERİ (TEK ÇEKİRDEK) olarak aranıyor...")
    baslangic_zamani_seri = time.time()
    seri_sonuclar = search_in_chunk(dizi_listesi, Aranan_Kelime)
    bitis_zamani_seri = time.time()
    seri_sure = bitis_zamani_seri - baslangic_zamani_seri
    print(f"✔ Seri arama {seri_sure:.2f} saniyede tamamlandı.\n")

    # --- 3. Adım: Paralel Arama ---
    print(f"'{Aranan_Kelime}' kelimesi PARALEL ({Cekirdek_Sayisi} ÇEKİRDEK) olarak aranıyor...")
    baslangic_zamani_paralel = time.time()

    # a) Listeyi çekirdek sayısı kadar parçaya böl
    # numpy.array_split bu iş için çok verimlidir.
    parcalar = np.array_split(dizi_listesi, Cekirdek_Sayisi)

    # b) İşçi havuzu oluştur
    # 'with' ifadesi, iş bitince havuzun otomatik olarak kapanmasını sağlar.
    with multiprocessing.Pool(processes=Cekirdek_Sayisi) as pool:
        # c) Görevi dağıt: Her bir parçayı search_in_chunk fonksiyonuna gönder
        # starmap, birden fazla argümanı olan fonksiyonlar için idealdir.
        # [(parça1, aranan_kelime), (parça2, aranan_kelime), ...] şeklinde veri hazırlar.
        paralel_sonuc_parcalari = pool.starmap(search_in_chunk, [(parca, Aranan_Kelime) for parca in parcalar])

    # d) Gelen sonuçları (liste içinde listeler) tek bir listede birleştir
    paralel_sonuclar = [item for sublist in paralel_sonuc_parcalari for item in sublist]
    
    bitis_zamani_paralel = time.time()
    paralel_sure = bitis_zamani_paralel - baslangic_zamani_paralel
    print(f"✔ Paralel arama {paralel_sure:.2f} saniyede tamamlandı.\n")

    # --- 4. Adım: Sonuçları ve Performans Karşılaştırmasını Gösterme ---
    print("="*25)
    print("     PERFORMANS SONUÇLARI")
    print("="*25)
    print(f"Seri Arama Süresi (1 Çekirdek):   {seri_sure:.4f} saniye")
    print(f"Paralel Arama Süresi ({Cekirdek_Sayisi} Çekirdek): {paralel_sure:.4f} saniye")
    
    try:
        hizlanma = seri_sure / paralel_sure
        print(f"\nHızlanma Oranı: {hizlanma:.2f}x")
        print(f"Paralel programlama, seri çalışmaya göre yaklaşık {int(round(hizlanma))} kat daha hızlı çalıştı.")
    except ZeroDivisionError:
        print("\nSüreler çok kısa olduğu için hızlanma oranı hesaplanamadı.")
        
    print(f"\nBulunan toplam eşleşme sayısı: {len(paralel_sonuclar)}")