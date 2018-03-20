def donembasi(koltuk,yatak,dolap):
    global donembasi
    donembasi=koltuk+yatak+dolap
    return donembasi

a = int(input("Koltuk sayısını giriniz:"))
b = int(input("Yatak sayısını giriniz:"))
c = int(input("Dolap sayısını giriniz:"))
d=donembasi(a,b,c)
print("Dönem başı stok:",donembasi)


def donemsonu(koltuk,yatak,dolap):
    global donemsonu
    donemsonu=koltuk+yatak+dolap
    return donemsonu

e=int(input("Koltuk sayısını giriniz:"))
f=int(input("Yatak sayısını giriniz:"))
g=int(input("Dolap sayısını giriniz:"))
h=donemsonu(e,f,g)
print("Dönem sonu stok:",donemsonu)
hesapla=(donembasi+donemsonu)/2
ort=format(float(hesapla),".0f")
print("Ortalama stok:",ort)
