# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:16:31 2019

@author: Arjun
"""

# In[] Soal No 1
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1.shp") #Digunakan untuk melakukan membaca file shp
print(sf) #menampilkan apa yang telah dipanggil pada variabel sf