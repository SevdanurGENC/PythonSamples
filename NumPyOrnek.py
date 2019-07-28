# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 01:11:44 2019

@author: Nano
"""
#NumPy (Numeric Python:Sayisal Python) Uygulamalari

import numpy as np
numpy_dizi = np.array(["Balikesir",1,"Isparta",2,"Kastamonu",3])
print(numpy_dizi)
olcum = [23,34,54,42,34,22,10,18,22]
olcum_np = np.array(olcum)
olcum_np = np.array([23,34,54,42,34,22,10,18,22])
olcum_np
print(olcum_np)

sinav_1 = [100,84,76,48,36,77,90]
sinav_2 = [95,78,66,57,75,89,95]
sinav_1_np = np.array(sinav_1)
sinav_2_np = np.array(sinav_2)
ortalama = (sinav_1_np+sinav_2_np)/2
print(ortalama)

sinav_1 + sinav_2
sinav_1_np + sinav_2_np
sinav_1_np[0]
sinav_2_np[3]

ortalama < 70
ortalama[ortalama < 70]

np.arange(1,11)
np.arange(1,11,2)
np.linspace(-2,2,21)
np.logspace(0,3,4)

dizi = np.arange(20)
print(dizi)
dizi[:7]
dizi[10:]
dizi[5:10]
dizi[::3]  #bastan itibaren 3'er 3'er

matris = dizi.reshape(4,5)
matris
matris[2:3,3:4]
matris[:2,:3]
matris.shape

dizi = np.array([[[2,3,4,5],
                 [6,7,8,9],
                 [10,11,12,13]],
                 [[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]]])
dizi.shape
print(dizi)

hisse = np.array([3.4,3.6,3.9,4.2,4.0,3.8])
type(hisse)
hisse_fiyat = np.array([[3.57,4.42,5.25,12.50,29.30],
                        [3.43,4.69,5.00,11.00,32.12],
                        [3.15,4.35,4.95,10.50,29.00]])
print(hisse_fiyat)
hisse_fiyat.shape
hisse_fiyat.T  #dizinin transpozunu alir
dizi.T

dizi.sum(0) #yukseklikleri toplar
dizi.sum(1) #satirlari toplar
dizi.sum(2) #sutunlari toplar

hisse_fiyat.cumsum(1) #satirlarin birikimli toplamlari

dizi.max()
dizi.argmax()
dizi.min()
dizi.argmin()
dizi.ptp()
dizi.clip(min,max)
dizi.round(a)
dizi.trace()
dizi.mean()
dizi.var()
dizi.std()
dizi.prod()
dizi.cumprod()
dizi.sort()

hisse_fiyat[1][3]
hisse_fiyat[1,3]
hisse_fiyat[0:2,:]
print(hisse_fiyat[0:2,2:4])

a = np.array([[3,4,7,4],
              [2,9,4,2],
              [1,5,8,3]])
b = np.array([[4,2,8,9],
              [6,3,6,1],
              [3,2,4,2]])
a+b
a-b
a/b
a*b

a
b
np.matmul(a,b)
np.sum(a[:,1])
np.mean(a[:,2])
np.median(a[1,:])

dizi = np.array([[2.34,3.76],
                [4.23,5.76],
                [1.18,9.32],
                [7.43,12.25],
                [3.14,2.78],
                [11.45,14.32],
                [5.78,4.43],
                [8.87,9.43]])
np.std(dizi[:,0])
np.corrcoef(dizi[:,0],dizi[:,1])

print(hisse_fiyat)

for i in hisse_fiyat:
    print(i)
for i in np.nditer(hisse_fiyat): #dizi icindeki elemanlara tek tek ulasir
    print(i)

#KULLANISLI NumPy METODLARI

x = np.random.uniform(low = 1, high = 50, size = 16).reshape(4,4)
x
np.amax(x,axis = 0)  #her sutundaki max deger
np.amax(x,axis = 1)  #her satirdaki max degers
np.amin(x,axis = 0)  #her sutundaki max deger
np.amin(x,axis = 1)  #her satirdaki max degers

x = np.array([4,2,1,6,9,3,15,11,10,7])
x
x.argsort() #dizi kucukten buyuge siralandiginda kacinci sirada olduklarini yazdirir

x = np.arange(1,7).reshape(3,2)
y = np.arange(7,13).reshape(3,2)
x
y
np.concatenate([x,y],axis = 0)   #dizileri satir yada sutun olarak birlestirir
np.concatenate([x,y],axis = 1)

np.full((3,2),2.5)  #verilen degeri istenen boyutlarda matris yapar

x = [1,3,5,7,9,11,13,15]
y = [3,6,9,11,13]
np.intersect1d(x,y)  #dizilerdeki ortak elemanlari ceker

x = [1,3,5,7]
dizi = [3,4,5,8,9,10]
np.isin(x,dizi) #verilen dizinin diger dizideki elemanlarin olup olmadigina dair bilgi verir

x = np.log([3,4,-5])
x
np.isnan(x)  #nan(not a number) degeri var mi yok mu gosterir

np.ones(3)   #1'de olusan matris veya diziler yazar
np.ones((3,2))

np.repeat(2,5)  #verilen degerden kac tane tekrarlanacak verilir

x = np.arange(1,13)
x
x.reshape(3,4)  #verilen dizinin satir ve sutun olarak yeniden duzenlenmesi

x = [1,3,5,7,9,11,13,15]
y = [3,6,9,11,13]
np.setdiff1d(x,y)  #bir dizide olup ikinci dizide olmayan elemanlari gosteri

x = np.array([3,4,6,3,2,2,3,4,2,2,4,3,3,2])
np.unique(x)   #birden fazla girilen degerleri teke indirir

dizi = np.arange(0,100)
dizi
np.where(dizi%10 == 0)   #verilen sarta gore dizi uzerinde islem yapip sonucunu yazdirir (10'a bolunen sayilari listele)

np.zeros(3)  #0'dan olusan dizi yada matris olusturmak icin kullanilir
np.zeros((3,2))