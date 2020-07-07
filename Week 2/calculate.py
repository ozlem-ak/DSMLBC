def topla(a,b):
    return a + b

def cikar(a,b):
    return a - b

def carp(a,b):
    return a * b

def bol(a,b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Bir sayıyı sıfıra bölemezsiniz. Lütfen sıfır dışında bir değer giriniz")
        
        
print( "Toplama : 1", "Çıkarma : 2" , "Çarpma : 3", "Bölme : 4")
islem = input("Hangi işlemi yapmak istersiniz?")

sayi_1 = int(input("1.Sayıyı giriniz : "))
sayi_2 = int(input("2.Sayıyı giriniz : "))

if islem == "1":
    print("İki sayının toplamı : " , topla(sayi_1, sayi_2))
    
elif islem == "2":
    print("İki sayının farkı : " , cikar(sayi_1, sayi_2))
       
elif islem == "3":
    print("İki sayının çarpımı : " , carp(sayi_1, sayi_2))
    
elif islem == "4":
    print("İki sayının bölümü : " , bol(sayi_1, sayi_2))
    
else:
    print("Lütfen işlemlerden birini seçiniz")