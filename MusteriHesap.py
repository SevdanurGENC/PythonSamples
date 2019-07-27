# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 00:48:26 2019

@author: Nano
"""

class Hesap():
    def __init__(self,hesap_no,hesap_sahibi,tutar=0):
        self.hesap_no = hesap_no
        self.hesap_sahibi = hesap_sahibi
        self.tutar = tutar
        
    def para_cek(self,cekilen):
        self.tutar -= cekilen
        
    def para_yatir(self, yatan):
        self.tutar += yatan
        
class Musteri():
    def __init__(self,musteri_no,adi,dogum_tarihi):
        self.musteri_no = musteri_no
        self.adi = adi
        self.dogum_tarihi = dogum_tarihi
        self.hesap1 = Hesap(12345,adi)
        
musteri_1 = Musteri(1111,'Sevdanur GENC','03.04.1983')
musteri_1
musteri_1.musteri_no
musteri_1.adi
musteri_1.hesap1.hesap_no
musteri_1.hesap1.hesap_sahibi
musteri_1.hesap1.tutar
musteri_1.hesap1.para_yatir(1250)
musteri_1.hesap1.tutar



