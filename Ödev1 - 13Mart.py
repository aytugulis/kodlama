#katma=Katma değer ciro
#toplam=Toplam satış miktarı
#ham=Hammadde maliyeti
#bakim=Bakım onarım giderleri
#sevkiyat=Sevkiyat giderleri
#satin=Satın alınan hizmet giderleri

def katma(toplam,ham,bakim,sevkiyat,satin):
    global katma
    katma=toplam-(ham+bakim+sevkiyat+satin)
    return katma


a=int(input("Toplam satış miktarını giriniz:"))
b=int(input("Hammadde maliyetini giriniz:"))
c=int(input("Bakım onarım giderini giriniz:"))
d=int(input("Sevkiyat giderini giriniz:"))
e=int(input("Satın alınan hizmet giderini giriniz:"))

fonk=katma(a,b,c,d,e)

if(katma>1000):
    print("İşletme katma değer cironuz yüksek.Katma değer cironuz:",katma)
elif(katma<500):
    print("İşletme katma değer cironuz düşük.Katma değer cironuz:",katma)
else:
    print("İşletme katma değer cironuz normal.Katma değer cironuz:",katma)
