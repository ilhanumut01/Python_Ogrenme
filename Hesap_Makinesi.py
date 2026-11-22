sayi1 = int(input("1.sayıyı giriniz:"))
sayi2 = int(input("2.sayıyı girniz:"))
islem = input("Yapılacak işlemi seçiniz( + , - , * , /):")



if (islem == "+" ):
    print(sayi1 + sayi2)
elif(islem == "-"):
    print(sayi1 - sayi2)
elif(islem == "*"):
    print(sayi1 * sayi2)    
elif(islem == "/"):
    print(sayi1 / sayi2)
else:
    print("Yanlış değer girdiniz !")  