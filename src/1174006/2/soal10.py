# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:46:11 2019

@author: vanerz
"""

print(1174006 % 8)

import shapefile #meng-import library shapefile

w = shapefile.Writer('soal10', shapeType=shapefile.POLYGON) #membuat object Writer baru dan memberi argumen berupa nama file dari shapefilenya yaitu soal10 dan argumen berupa shapeTypenya yaitu shapefile.POLYGON yang berupa poligon
w.shapeType #menentukan shapeTypenya

w.field("kolom1", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom1 dan tipe datanya yaitu char
w.field("kolom2", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom2 dan tipe datanya yaitu char

w.record("nmax", "duar") #mengisi data pada field yang telah dibuat yaitu kolom1 = nmax dan kolom2 = duar

w.poly([[[1,1],[4,1],[6,-2],[-1,-2],[1,1]]]) #mengisi data poly sesuai koordinatnya masing-masing

w.close() #menutup file