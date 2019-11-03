# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:02:52 2019

@author: Rifky
"""

# In[] Soal No 11
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal2.shp") #Digunakan untuk melakukan membaca file shp
isidata = sf.records() #membaca seluruh data yang ada di dalam file shp tersebut
print(isidata[0]) #menampilkan data pada index ke 0
print(isidata[0][0]) #menampilkan data pada index ke 0 dan urutan ke 0