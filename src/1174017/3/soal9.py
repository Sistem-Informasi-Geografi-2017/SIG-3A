# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:02:52 2019

@author: Rifky
"""

# In[] Soal No 9
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal9.shp") #Digunakan untuk melakukan membaca file shp
namakolom = sf.fields #Digunakan untuk membca field yang ada pada file SHP Tersebut
print(namakolom) # Digunakan Untuk menampilkan field tersebut