mystring = "MERHABA"
# print(mystring[0])   # kelimedeki harfi yazdırır
# print(mystring[1:3]) # ER harflerini yazdırma
# MRA
# print(mystring[0:5:2])
"""
STRİNGLERİ EKLEME
str1 = "merhaba"
str2 = "dünya"
str3 = str1 + " " + str2
print(str3)
"""
str1 = "merhaba dünya"
str_buyukharfler = str1.upper() # ifadenin bütün harflerini büyük hale getirir
print(str_buyukharfler) 

str_kucukharfler = str_buyukharfler.lower()
print(str_kucukharfler)         # ifadenin bütün harflerini kucuk hale getirir

print(str1.split()) # ['merhaba', 'dünya'] kelimleri ayırıyor
# print(str1.split(",")) kelimeler ',' ile ayrıysa böyle ayrılmalı