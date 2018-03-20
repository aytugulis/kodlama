#mcs16=Müşteri Çalışma Süreleri-2016
#cs16=Çalışma Süreleri-2016
#tms16=Toplam Müşteri Sayıları-2016
#mcs17=Müşteri Çalışma Süreleri-2017
#cs17=Çalışma Süreleri-2017
#tms17=Toplam Müşteri Sayısı-2017

cs16=170
tms16=50
cs17=cs16+50
tms17=tms16+20

def mcs16(cs16,tms16):
    mcs16=cs16/tms16
    return mcs16

def mcs17(cs17,tms17):
    mcs17=cs17/tms17
    return mcs17

hesapla=mcs16(cs16,tms16)-mcs17(cs17,tms17)
cevap=format(float(hesapla))
print("2016-2017 yılları arasındaki müşterilerle çalışma sayısı farkı:",cevap)
