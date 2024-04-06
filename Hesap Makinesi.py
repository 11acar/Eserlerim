while True:
    sayi1 = input("1.sayı:")

    if not sayi1.isdigit():
        print("Lütfen sayıyı doğru giriniz!")


islem= input("İşlem:")
while True:
    if islem=="+":
        break
    elif islem=="-":
        break
    elif islem=="*":
        break
    elif islem=="/":
        break
    else:
        if islem != "+":
            if islem != "-":
                if islem != "*":
                    if islem != "/":
                        print("!!!Lütfen işlem bölümüne + , - , * , /  karakterlerini giriniz!!!")
                        islem= input("İşlem:")
                        continue

while True:
    sayi2= input("2.sayı:")

    if not sayi2.isdigit():
        print("Lütfen sayıyı doğru giriniz!")



sayi1, sayi2= int(sayi1), int(sayi2)

if islem=="+":
    print(sayi1+sayi2)
elif islem=="-":
    print(sayi1-sayi2)
elif islem=="*":
    print(sayi1*sayi2)
elif islem=="/":
    if sayi2 == 0:
        print("Tanımsız! (Lütfen sayınızı 0 haricinde bir sayıya bölünüz!)")
    else:
        print(sayi1 / sayi2)


