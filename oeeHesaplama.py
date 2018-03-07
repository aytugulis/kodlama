#a=Planlanmış üretim süresi , b=Plansız duruş

def kullanilabilirlik():
    a=int(input("Planlanmış üretim süresini giriniz:"))
    b=int(input("Plansız duruşu giriniz:"))
    kul=((a-b)/a)
    return print("Kullanılabilirlik:",kul)

#c=Standart çevrim zamanı , d=Üretim miktarı , a=Planlanmış üretim süresi , b=Plansız duruş , e=

def performans():
    c=int(input("Standart çevrim zamanını giriniz:"))
    d=int(input("Üretim miktarını giriniz:"))
    a=int(input("Planlanmış üretim süresini giriniz:"))
    b=int(input("Plansız duruşu giriniz:"))
    per=((c*d)/(a-b))
    return print("Performans",per)

#e=Sağlam ürün miktarı , f=Toplam üretim miktarı

def kalite():
    e=int(input("Sağlam ürün miktarını giriniz:"))
    f=int(input("Toplam üretim miktarını giriniz:"))
    kal=(e/f)
    return print("Kalite",kal)

#Herhangi bir ayrı değişken yok üstteki değişkenleri yazıyoruz.

def OEE():
    a=int(input("Planlanmış üretim süresini giriniz:"))
    b=int(input("Plansız duruşu giriniz:"))
    kul=((a-b)/a)
    c=int(input("Standart çevrim zamanını giriniz:"))
    d=int(input("Üretim miktarını giriniz:"))
    per=((c*d)/(a-b))
    e=int(input("Sağlam ürün miktarını giriniz:"))
    f=int(input("Toplam üretim miktarını giriniz:"))
    kal=(e/f)
    oee=(kul*per*kal)
