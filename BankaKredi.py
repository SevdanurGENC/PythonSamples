# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 22:05:03 2019

@author: Nano
"""

class Banka_Hesabi():
    def __init__(self,hesap_no,hesap_sahibi,tutar):
        self.hesap_no = hesap_no
        self.hesap_sahibi = hesap_sahibi
        self.tutar = tutar
        
    def para_cek(self,cekilen):
        if self.kalan_limit - cekilen > 0:
            self.tutar -= cekilen
            self.kalan_limit -= cekilen
        else:
            print("Yeterli kredi limitiniz bulunmamaktadir.\n")
            print("Kullanilabilir limitiniz : " + str(self.kalan_limit))
        
    def para_yatir(self,yatan):
        self.tutar += yatan
        
class Kredili_Hesap(Banka_Hesabi):
    def __init__(self,hesap_no,hesap_sahibi,limit,tutar=0):
        super().__init__(hesap_no,hesap_sahibi,tutar)
        self.limit = limit
        
hesap_001 = Banka_Hesabi(1,"Sevdanur GENC",100)
print(hesap_001.hesap_no)
print(hesap_001.hesap_sahibi)
print(hesap_001.tutar)

hesap_001.para_cek(50)
print(hesap_001.tutar)

hesap_001.para_yatir(180)
print(hesap_001.tutar)        
        
kredi_hesabi_001 = Kredili_Hesap(hesap_no=2, hesap_sahibi="Sevdanur GENC",limit=500)
kredi_hesabi_001.limit
kredi_hesabi_001.kalan_limit
kredi_hesabi_001.tutar
kredi_hesabi_001.para_cek(150)
kredi_hesabi_001.tutar
kredi_hesabi_001.kalan_limit
kredi_hesabi_001.para_cek(400)