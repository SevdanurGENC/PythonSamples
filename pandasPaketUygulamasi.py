# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:03:38 2019

@author: Nano
"""

#pandas paketiyle ilgili çalışmalar.
#pandas serilerinin oluşturulması
import pandas as pd
pandas_seri = pd.Series([5,7,3,10,8,6])
pandas_seri
type(pandas_seri)
pandas_seri = pd.Series([5,7,3,10,8,6], index = ['a','b','c','d','e','f'])
pandas_seri['c':'e']

#pandas veri çerçevelerinin oluşturulması
iris_dict = {
        'Sepal_Length' : [5.1,4.9,4.7,4.6,5.0,6.7,6.3,6.5,6.2,5.9],
        'Sepal_Width' : [3.5,3.0,3.2,3.1,3.6,3.0,2.5,3.0,3.4,3.0],
        'Petal_Length' : [1.4,1.4,1.3,1.5,1.4,5.2,5.0,5.2,5.4,5.1],
        'Petal_Width' : [0.2,0.2,0.2,0.2,0.2,2.3,1.9,2.0,2.3,1.8],
        'Species' : ['setosa','setosa','setosa','setosa','setosa',
                     'virginica','virginica','virginica','virginica','virginica']} 
iris_dict
import pandas as pd
iris = pd.DataFrame(iris_dict) 
print(iris)

Sepal_Length = [5.1,4.9,4.7,4.6,5.0,6.7,6.3,6.5,6.2,5.9]
Sepal_Width = [3.5,3.0,3.2,3.1,3.6,3.0,2.5,3.0,3.4,3.0]
Petal_Length = [1.4,1.4,1.3,1.5,1.4,5.2,5.0,5.2,5.4,5.1]
Petal_Width = [0.2,0.2,0.2,0.2,0.2,2.3,1.9,2.0,2.3,1.8]
Species = ['setosa','setosa','setosa','setosa','setosa','virginica','virginica','virginica','virginica','virginica']
liste_etiketleri = ['Sepal_Length','Sepal_Width','Petal_Width','Petal_Length','Species']
sutunlar =  [Sepal_Length,Sepal_Width,Petal_Length,Petal_Width]
zip_veri = list(zip(liste_etiketleri,sutunlar))
print(zip_veri)
veri = dict(zip_veri)
print(veri)
iris = pd.DataFrame(veri)
print(iris)

iris['Gözlem_No'] = 1
print(iris)

import pandas as pd
iris = pd.read_csv("C:/Users/Nano/Documents/pytDers/DataSets/iris.csv")
type(iris)
iris.columns
iris.columns = ['Taç Boy', 'Taç En','Çanak Boy',
                'Çanak En','Tür']
print(iris)
iris.head(10)
iris.tail(4)
print(iris.tail(4))

iris.index
iris.shape
iris.info()
iris_yeni = iris.copy()
np_dizi = iris.values   #NumPy dizinine çevirmek için kullanılır.
print(np_dizi)

import numpy as np
dizi = iris.iloc[:,[0,1,2,3]]
dizi_log = np.log(dizi)
print(dizi_log.head())

import pandas as pd
indeks = [('ABC',2016),('ABC',2017),
          ('DEF',2016),('DEF',2017),
          ('XYZ',2016),('XYZ',2017),
          ('KLM',2016),('KLM',2017)]
fiyatlar = [32.5,12.3,24.7,18.6,20.3,7.2,51.9,56.2]
hisseler = pd.Series(fiyatlar, index=indeks)
hisseler
hisseler[('XYZ',2016):('KLM',2017)]

indeks = pd.MultiIndex.from_tuples(indeks)
indeks
hisseler = pd.Series(fiyatlar,index=indeks)
hisseler
hisseler.index.names = ['Hisse','Yıl']
hisseler

hisseler.unstack() #dataframe'in boyoutlarındaki şekli değiştirir
hisseler.stack()
hisseler

pd.MultiIndex.from_tuples([('x',1),('x',2),('y',1),('y',2)])
pd.MultiIndex.from_arrays([['x','x','y','y'],[1,2,1,2]])
pd.MultiIndex.from_product([['y','y'],[1,2]])

indeks = pd.MultiIndex.from_product([['ABC','DEF','KLM'],[2016,2017]])
sutunlar = pd.MultiIndex.from_product([['Q1','Q2','Q3','Q4'],['Hacim','Kapanış']])
veri = np.array([10762,32.5,12638,33.5,13689,35.2,18414,37.4,
                 10688,12.3,14348,13.2,15924,15.3,15243,17.9,
                 14841,24.7,14966,22.1,13098,19.3,17439,15.4,
                 15607,18.6,16166,13.4,10627,15.1,13396,15.3,
                 12565,20.3,17469,21.4,18964,22.5,15187,23.6,
                 13203,7.2,10629,7.2,15239,8.2,18307,9.1])
veri = np.reshape(veri,(6,8))
hisseler = pd.DataFrame(veri, index=indeks, columns=sutunlar)
hisseler

#dataframede seçim yapma
import pandas as pd
iris = pd.read_csv("C:/Users/Nano/Documents/pytDers/DataSets/iris.csv")
type(iris)
iris["sepal.length"]
print(iris)
type(iris["sepal.length"])
iris[["sepal.length","sepal.width"]]
iris[2:5]

hisseler.loc["ABC"]
hisseler.loc[["ABC"]]
hisseler.loc[["ABC","KLM"]]
hisseler.loc['Hacim Kapanış']['ABC']
hisseler.iloc[[1]]
hisseler.iloc[5,0]
hisseler.iloc[[1,2,3]]
hisseler.loc[["ABC","KLM"]]
hisseler.loc[["KLM":"ABC":-1]]

#pandas ile veri analizi
import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()
iris.describe()
iris['species'].describe()
iris['species'].unique()
iris.count()
iris[['petal_length','petal_width']]
veriler = ['petal_length','petal_width']
veriler
iris[veriler].count()
iris.std()
iris.quantile(0.25)
iris.quantile([0.25,0.75])
iris['petal_length'].min()
iris['petal_width'].max()
iris.mean(axis='columns')
iris.std(axis='columns')

kosul = iris['species'] == 'versicolor'
type(kosul)
kosul
versicolor = iris.loc[kosul,:]
versicolor.head()
versicolor.describe()
iris[iris['species'] == 'virginica'].describe()

import pandas as pd
iris = pd.read_csv("C:/Users/Nano/Documents/pytDers/DataSets/iris.csv")
kosul = iris['species'].str.contains('setosa')
iris.head()
setosa = iris[kosul]
print(setosa.head())
iris[iris.sepal_length>7.5]
iris[(iris.sepal_length>6.5) & (iris.petal_length<4.5)]
iris[(iris.sepal_length>7.5) | (iris.petal_length>6.5)]
iris.petal_length[iris.sepal_length>7.5]

import pandas as pd
import numpy as np
degisken = np.repeat(['A','B','C','D'],[3,3,3,3],axis = 0)
deger = np.random.random(12)
df_dict = {'degisken':degisken, 'deger':deger}
df = pd.DataFrame(df_dict)
df = df[['degisken','deger']]
print(df)
df2 = df.pivot(columns = 'degisken', values = 'deger')
print(df2)
df3 = df2.melt(value_vars=['A','B','C','D'],value_name='deger').dropna()
print(df3)

d1 = [('Ali','Baran','Mehmet',97,85,76), column = 2, rows=3]
d1.columns('X','Y1')


