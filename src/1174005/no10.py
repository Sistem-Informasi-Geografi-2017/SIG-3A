# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:12:24 2019

@author: ONIWALDUS
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor10', shapeType=5) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor10 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("C1","C") # Membuat table dengan kolom pertama
w.field("C2","C") # Membuat table dengan kolom kedua
 
w.record("Oniwaldus","BereMali")     #Mengisi table pada kolom satu yaitu Andmesh dan kolom dua yaitu Indonesia


w.poly([[[-2,1],[7,1],[7,13],[-2,1]]]) # Membuat garis dengan menghubungkan titik-titik sehingga nantinya akan membentuk sebuah bidang

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan
