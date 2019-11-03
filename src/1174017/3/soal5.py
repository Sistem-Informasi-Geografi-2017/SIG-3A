# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:02:52 2019

@author: Rifky
"""

# In[] Soal No 5
import shapefile #mengimport shapefile
sf = shapefile.Reader("soal5.shp") #membaca file shp yang bernama Soal5.shp
sp = sf.shapes() # untuk membaca shapes
print(dir(sp[0])) # untuk menampilkan fungsi - fungsi di dir dari index 0
print(dir(sp)) # untuk menampilkan fungsi - fungsi di dir