mylist = [1, 2, 3, 4, 5]
  
"""
def kupunu_al(x):
    return (x**3)

# for i in mylist:
#    print(kupunu_al(i))

# map
yenilist = list(map(kupunu_al,mylist))
print(yenilist)

# lambda
yeniliste2 = list(map(lambda sayi: sayi**3, mylist))
print(yeniliste2)
"""

#filter
def tek_sayilari_filtrele(n):
    if (n % 2 == 1):
        return n
    else:
        return None

yeni_liste3 = list(filter(tek_sayilari_filtrele,mylist))
print(yeni_liste3)  
 