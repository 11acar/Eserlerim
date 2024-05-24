#hesap makinesi v2.2

import os

def terminali_temizle():
    if os.name == 'nt':
        _ = os.system('cls')

terminali_temizle()
    

error = "Lütfen geçersiz karakter girmeyiniz!" 

print("Kullanım listesini görmek için \"support\" yazınız!")
support_list = ["-----------------", "+   : Toplama", "-   : Çıkarma", "*   : Çarpma", "/   : Bölme", "**  : Üs alma", "//  : Tam sayı bölme", "/*  : Karekök", "*** : Faktöriyel", "*/  : Çarpmaya göre tersi", "-----------------"]
cift_islem = ["+", "-", "*", "/", "**", "//"]
tek_islem = ["/*", "***", "*/"]

while True:
    sayi1 = input("1.Sayı:")
    if sayi1 == "support":
        for i in support_list:
            print(i)
        continue
    elif not sayi1.isdigit():
        print(error)
        continue
    else:
        sayi1 = int(sayi1)
        break
while True:
    islem = input("İşlem:")
    if islem == "support":
        for i in support_list:
            print(i)
        continue
    elif islem in cift_islem or islem in tek_islem:
        break
    else:
        print(error)
        continue
while True:
    if islem in tek_islem:
        break
    sayi2 = input("2.Sayı:")
    if islem == "support":
        for i in support_list:
            print(i)
        continue
    elif not sayi2.isdigit():
        print(error)
        continue
    else:
        sayi2 = int(sayi2)
        break
import acrmath
if islem == "+":
    sonuc = acrmath.toplama(sayi1, sayi2)
elif islem == "-":
    sonuc = acrmath.cikarma(sayi1, sayi2)
elif islem == "*":
    sonuc = acrmath.carpma(sayi1, sayi2)
elif islem == "/":
    sonuc = acrmath.bolme(sayi1, sayi2)
elif islem == "**":
    sonuc = acrmath.us(sayi1, sayi2)
elif islem == "//":
    sonuc = acrmath.tam_sayi_bolmesi(sayi1, sayi2)
elif islem == "/*":
    sonuc = acrmath.karekok(sayi1)
elif islem == "***":
    sonuc = acrmath.faktoriyel(sayi1)
elif islem == "*/":
    sonuc = acrmath.carpma_tersi(sayi1)

print(f"Sonuç: {sonuc}")

import time

while True:
    import os

    def terminali_temizle():
        if os.name == 'nt':
            _ = os.system('cls')

    terminali_temizle()

    print(f"1.Sayı:{sonuc}")

    while True:
        islem = input("İşlem:")
        if islem == "stop":
            break
        elif islem == "support":
            for i in support_list:
                print(i)
            continue
        elif islem in cift_islem or islem in tek_islem:
            break
        else:
            print(error)
            continue

    if islem == "stop":
        print("Ending...")
        time.sleep(1)
        break

    while True:
        if islem in tek_islem:
            break
        sayi2 = input("2.Sayı:")
        if sayi2 == "stop":
            break
        elif sayi2 == "support":
            for i in support_list:
                print(i)
            continue
        elif not sayi2.isdigit():
            print(error)
            continue
        else:
            sayi2 = int(sayi2)
            break

    if islem == "stop":
        print("Ending...")
        time.sleep(1)
        break

    import acrmath

    if islem == "+":
        sonuc = acrmath.toplama(sonuc, sayi2)
    elif islem == "-":
        sonuc = acrmath.cikarma(sonuc, sayi2)
    elif islem == "*":
        sonuc = acrmath.carpma(sonuc, sayi2)
    elif islem == "/":
        sonuc = acrmath.bolme(sonuc, sayi2)
    elif islem == "**":
        sonuc = acrmath.us(sonuc, sayi2)
    elif islem == "//":
        sonuc = acrmath.tam_sayi_bolmesi(sonuc, sayi2)
    elif islem == "/*":
        sonuc = acrmath.karekok(sonuc)
    elif islem == "***":
        sonuc = acrmath.faktoriyel(sonuc)
    elif islem == "*/":
        sonuc = acrmath.carpma_tersi(sonuc)

    print(f"Sonuç: {sonuc}")