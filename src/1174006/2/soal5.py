# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:21:09 2019

@author: vanerz
"""

import shapefile #meng-import library shapefile

w = shapefile.Writer('soal5') #membuat object Writer baru dan memberi argumen berupa nama file dari shapefilenya yaitu soal5
w.shapeType #menentukan shapeTypenya

w.field("kolom1", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom1 dan tipe datanya yaitu char
w.field("kolom2", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom2 dan tipe datanya yaitu char

w.record("ngek", "satu") #mengisi data pada field yang telah dibuat yaitu kolom1 = ngek dan kolom2 = satu

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #mengisi data line sesuai koordinatnya masing-masing

w.close() #menutup file