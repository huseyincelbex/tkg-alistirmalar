# Hafta 2: Python temelleri
def isaret(sayi):
    if sayi > 0:
        return "pozitif"
    elif sayi < 0:
        return "negatif"
    else:
        return "sıfır"

def donem_notu(vize, final):
    return (vize * 0.4) + (final * 0.6)

def harf_say(metin, harf):
    return metin.count(harf)

def faktoriyel(n):
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

def gecenler(notlar):
    return [not_ for not_ in notlar if not_ >= 60]
