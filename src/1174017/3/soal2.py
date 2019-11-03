# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:02:52 2019

@author: Rifky
"""

# In[] Soal No 2
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal2.shp") #Digunakan untuk melakukan membaca file shp
st= sf.shapeType #Untuk mengetahui Type dari file SHP yang dibaca
print(st)