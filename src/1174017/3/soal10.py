# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:02:52 2019

@author: Rifky
"""

# In[] Soal No 10
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1.shp") #Digunakan untuk melakukan membaca file shp
isidata = sf.records() #membaca seluruh data yang ada di dalam file shp tersebut
print(isidata) #menampilkan data tersebut