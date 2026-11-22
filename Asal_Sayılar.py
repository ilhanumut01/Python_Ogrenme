def asal_mi(sayi):
    if (sayi <= 1):
       return False
    for i in range(2,sayi):
        if (sayi % i) == 0:
            return False
    return True


# print(asal_mi())


for x in range(1,101):
    if (asal_mi(x)):
        print(x, end=" ")