#Gelirler;a=Finansman geliri , b=Pazar geliri , c=Kira geliri

a=int(input("Finansman gelirini giriniz:"))
b=int(input("Pazar gelirini giriniz:"))
c=int(input("Kira gelirini giriniz:"))

#Giderler;d=Ücret gideri , e=Finansman gideri , f=Pazar gideri , g=Kira gideri , h=Muhasebe gideri

d=int(input("Ücret giderini giriniz:"))
e=int(input("Finansman giderini giriniz:"))
f=int(input("Pazar giderini giriniz:"))
g=int(input("Kira giderini giriniz:"))
h=int(input("Muhasebe giderini giriniz:"))

kar=(a+b+c)-(d+e+f+g+h)
zarar=-(a+b+c)+(d+e+f+g+h)


if(int(kar)>1000):
    print("İşletme karlı durumda,Edilen kar:",kar)
    
elif(int(kar)==1000):
    print("İşletme ne kar ne zarar etmiştir.")
      
else:
    print("İşletme karlı durumda değil edilen zarar:",zarar)
