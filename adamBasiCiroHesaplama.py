#a=Satış miktarı , b=Birim satış fiyatı

def adambasiciro():
    a=int(input("Satış miktarını giriniz:"))
    b=int(input("Birim satış fiyatını giriniz:="))
    ciro=(a*b)
    adambasiciro=(ciro)/25
    return print("Adambaşına düşen ciro=",adambasiciro)
