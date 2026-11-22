# karesi 81 olan sayının sırası bulunuz ve ekrana yazdırız


sayilar = [ 4, 7, 9, 2, 11 ]


index = 0
for no in sayilar:
    karesi = no * no
    if (karesi == 81):
        break
    index = index + 1
print(index,".index", "değer:",sayilar[index])    
       