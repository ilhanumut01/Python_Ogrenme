import re

cumle = "Modüler yapısı, sınıf dizgesini (sistem) ve her türlü veri alanı girişini destekler. Hemen hemen her türlü platformda çalışabilir (Unix, Linux, Mac, Windows, Amiga, Symbian). Python ile sistem programlama, kullanıcı arabirimi programlama, ağ programlama, web programlama, uygulama ve veritabanı yazılımı programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük yazılımların hızlı bir şekilde prototiplerinin üretilmesi ve denenmesi gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir.Python 1980'lerin sonunda ABC programlama diline alternatif olarak tasarlanmıştı. Python 2.0, ilk kez 2000 yılında yayınlandı.2008 de yayınlanan Python 3.0, dilin önceki versiyonuyla tam uyumlu değildir ve Python 2.x'te yazılan kodların Python 3.x'te çalışması için değiştirilmesi gerekmektedir. Python 2 versiyonun resmi geliştirilme süreci, dilin son sürümü olan Python 2.7.x serisi versiyonların ardından 1 Ocak 2020 itibarıyla resmi olarak sona erdi. Python 2.x geliştirilme desteğinin sona ermesinin ardından, Python dilinin 3.7.x ve sonraki sürümlerinin geliştirilmesi devam etmektedir."

patern = "Python"
"""
sonuc = re.search(patern, cumle)           İlk bulduğu kelimede durur
print(sonuc.start(), " ", sonuc.end())
"""
cout = 0

for bulunan in re.finditer(patern, cumle):  # büyük metinlerdeki istenen kelimenin
    print(bulunan.span(), bulunan.group())  # hangi karakter aralığında olduğunu gösterir
    cout += 1

# print("Toplamda aranan kelime","(", patern, ")", cout, "kez kullanılmıştır")  

# Desen eşleştirme  
cumle2 = "Merhaba benim cep numaram 532-1112233 beni öğleden sonra arıyabilirsiniz.."

# rakamlar için \d
# harfler için \w
# boşluk için \s
#....

patern2 = "\d\d\d-\d\d\d\d\d\d\d"
print(re.search(patern2, cumle2))