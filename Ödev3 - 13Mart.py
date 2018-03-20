def ilk6(iyg,ifg,iusg,icm,ikg,idm):
    global ilk6
    ilk6=(iyg+ifg+iusg)-(icm+ikg+idm)
    return ilk6
iyg=int(input("İlk 6 ay yazılım gelirini giriniz:"))
ifg=int(input("İlk 6 ay finansal gelirini giriniz:"))
iusg=int(input("İlk 6 ay ürün satış gelirini giriniz:"))
icm=int(input("İlk 6 ay çalışan maaşlarını giriniz:"))
ikg=int(input("İlk 6 ay kira giderlerini giriniz:"))
idm=int(input("İlk 6 ay donanım maliyetlerini giriniz:"))
ilk6(iyg,ifg,iusg,icm,ikg,idm)
print("İlk 6 aylık karınız:",ilk6)

def son6(syg,sfg,setg,susg,scm,skg,sdm):
    global son6
    son6=(syg+sfg+susg)-(scm+skg+sdm)
    return son6
syg=int(input("Son 6 ay yazılım gelirlerini giriniz:"))
sfg=int(input("Son 6 ay finansal gelirlerini giriniz:"))
setg=int(input("Son 6 ay e ticaret gelirlerini giriniz:"))
susg=int(input("Son 6 ay ürün satış gelirlerini giriniz:"))
scm=int(input("Son 6 ay çalışan maaşlarını giriniz:"))
skg=int(input("Son 6 ay kira giderlerini giriniz:"))
sdm=int(input("Son 6 ay donanım maliyetlerini giriniz:"))
son6(syg,sfg,setg,susg,scm,skg,sdm)
print("Son 6 aylık karınız:",son6)

fark=son6-ilk6

if(fark>5000):
      print("İşletme çok karda,karlılık=",fark)

elif(fark<1000):
      print("İşletme yeterince karda değil,karlılık=",fark)

else:
      print("İşletme normal karda,karlılık=",fark)
