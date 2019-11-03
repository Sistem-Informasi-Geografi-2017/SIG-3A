# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:02:52 2019

@author: Rifky
"""

# In[] Soal No 8
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal8.shp") #Digunakan untuk melakukan membaca file shp
anu=sf.shape(0) #Digunakan untuk membaca jumlah data yang ada di file shp tersebut dan index ke 0
anu.points #Menampilkan Koordinat yang ada pada baris tersebut
print(anu)