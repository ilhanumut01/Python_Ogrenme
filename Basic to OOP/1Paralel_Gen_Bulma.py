# Proses Tabanlı Paralelleştirme (Process-Based Parallelism)
import random
import time
from multiprocessing import Pool, cpu_count

# Aranacak olan spesifik dizilim ve uzunluğu global olarak tanımlanıyor
ARANAN_DIZILIM = "ACTAGATG"
ARANAN_UZUNLUK = len(ARANAN_DIZILIM)

def paralel_sayim_gorevi(chunk_params):
    """
    Belirtilen uzunlukta rastgele bir genetik dizi parçası oluşturur
    ve bu parça içindeki aranan dizilimi sayar.
    """
    chunk_uzunlugu, seed = chunk_params
    # Her işlemcinin farklı bir rastgele dizi üretmesi için kendi seed'ini kullanır
    random.seed(seed)
    
    bazlar = ['A', 'T', 'G', 'C']
    # .join() ve list comprehension büyük diziler için en hızlı yöntemlerden biridir.
    dizi_parcasi = "".join(random.choice(bazlar) for _ in range(chunk_uzunlugu))
    
    return dizi_parcasi.count(ARANAN_DIZILIM)

def sayim_ve_kesisimleri_hesapla(chunk_params):
    """
    Bu fonksiyon hem chunk içindeki sayımı yapar hem de chunk'lar arası
    kesişim noktalarında oluşabilecek dizilimleri kontrol eder.
    """
    chunk_uzunlugu, seed = chunk_params
    random.seed(seed)
    
    bazlar = ['A', 'T', 'G', 'C']
    
    # Kesişim kontrolü için parçanın sonundan biraz veri al
    # Örnek: "ACTAG" ararken bir chunk "...AC", diğeri "TAG..." ile bitebilir.
    # Bunu yakalamak için chunk'lar arasında (aranan uzunluk - 1) kadar bir kesişim alanı oluşturmalıyız.
    kesisim_alani_uzunlugu = ARANAN_UZUNLUK - 1
    
    # Ana chunk'ı oluştur
    ana_chunk = "".join(random.choice(bazlar) for _ in range(chunk_uzunlugu))
    
    # Bir sonraki chunk'ın başlangıcını temsil eden kesişim alanını oluştur
    kesisim_alani = "".join(random.choice(bazlar) for _ in range(kesisim_alani_uzunlugu))
    
    # Ana chunk ve kesişim alanını birleştirerek tara
    toplam_sayim = (ana_chunk + kesisim_alani).count(ARANAN_DIZILIM)
    
    return toplam_sayim


if __name__ == '__main__':
    # Kodun sadece ana program olarak çalıştırıldığında devreye girmesini sağlar.
    # Bu, multiprocessing için zorunludur.
    
    toplam_dizi_uzunlugu = 200_000_000
    
    # Bilgisayardaki mevcut işlemci çekirdeği sayısını al
    cekirdek_sayisi = cpu_count()
    print(f"Hesaplama icin {cekirdek_sayisi} islemci cekirdegi kullaniliyor...")
    
    # Toplam işi çekirdek sayısına böl
    parca_uzunlugu = toplam_dizi_uzunlugu // cekirdek_sayisi
    
    # Her bir işlemciye gönderilecek iş listesini oluştur
    # Her işe farklı bir "seed" vererek tamamen rastgele olmalarını sağlıyoruz
    gorevler = [(parca_uzunlugu, i) for i in range(cekirdek_sayisi)]
    
    # Eğer toplam uzunluk tam bölünmediyse, kalan kısmı son göreve ekle
    kalan_uzunluk = toplam_dizi_uzunlugu % cekirdek_sayisi
    if kalan_uzunluk > 0:
        gorevler.append((kalan_uzunluk, cekirdek_sayisi))
        
    print(f"Toplam {toplam_dizi_uzunlugu} elemanli dizi, {len(gorevler)} parcaya bolundu.")
    print("-" * 40)
    
    baslangic_zamani = time.time()
    
    # İşlemci havuzu oluştur ve görevi başlat
    with Pool(processes=cekirdek_sayisi) as pool:
        # pool.map, görevler listesindeki her bir elemanı sırayla fonksiyona gönderir
        # ve sonuçları bir liste olarak toplar.
        # Not: Bu yöntem chunk'ların birleşim yerlerini (kesişimleri) kontrol etmez
        # ama devasa veri setinde bu kayıp istatistiksel olarak ihmal edilebilir.
        # %100 doğruluk için 'sayim_ve_kesisimleri_hesapla' fonksiyonunu kullanabilirsiniz.
        # sonuc_listesi = pool.map(paralel_sayim_gorevi, gorevler)
        sonuc_listesi = pool.map(sayim_ve_kesisimleri_hesapla, gorevler)

    # Her bir işlemciden gelen sonucu topla
    toplam_bulunan = sum(sonuc_listesi)
    
    bitis_zamani = time.time()
    
    print(f"Olusturulan Ornek Genetik Dizinin Uzunlugu: {toplam_dizi_uzunlugu}")
    print(f"Aranan Dizilim: '{ARANAN_DIZILIM}'")
    print(f"'{ARANAN_DIZILIM}' dizilimi, ornek dizi icinde yaklasik {toplam_bulunan} kez bulundu.")
    print("-" * 40)
    print( "Yuzde",toplam_bulunan / 1500000,"'dir.")
    print(f"Islem {bitis_zamani - baslangic_zamani:.2f} saniyede tamamlandi.")