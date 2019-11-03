# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:04:18 2019

@author: Sujadi
"""

import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
print(sf) #menampilkan apa yang telah dipanggil pada variabel sf
# In[] No 2