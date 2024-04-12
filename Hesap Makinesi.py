#hesap makinesi v1.6

print(""">Yüzde hesaplamak için \"%\" yazınız.
>Üs almak için işlem bölümüne \"**\" yazınız.""")

while True:
    sayi1= input("1.Sayı:")
    if sayi1== "%":
        x = int(input("Sayı:"))
        y = int(input("%"))
        z = y / 100
        sonuc = x * z
        print("Sonuç:", sonuc)
        break
    elif not sayi1.isdigit():
        print("Lütfen geçerli bir tam sayı giriniz!")
        continue
    else:
        sayi1= int(sayi1)
        break

while True:
    if sayi1=="%":
        break
    islem= input("İşlem:")
    if islem in ["+", "-", "*", "/", "**"]:
        break
    else:
        print("Lütfen geçerli bir işlem giriniz! ( + , - , * , / , ** )")
        continue

while True:
    if sayi1=="%":
        break
    sayi2= input("2.Sayı:")
    if not sayi2.isdigit():
        print("Lütfen geçerli bir tam sayı giriniz!")
        continue
    else:
        sayi2= int(sayi2)
        break

while True:
    if sayi1=="%":
        break
    else:
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            sonuc = sayi1 / sayi2
        elif islem == "**":
            sonuc = sayi1 ** sayi2
        break

while True:
    if sayi1=="%":
        break
    else:
        print(sonuc)
        break
