# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:09:32 2019

@author: ONIWALDUS
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor2', shapeType=1)  # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor2 dan bentuknya itu adalah shapetype 1 yaitu point (titik)
 
w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua
 
w.record("ngek","satu") # Mengisi untuk table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2
w.record("ngok","dua")  # Mengisi untuk table yaitu ngok adalah isi pada kolom1 dan satu adalah isi pada kolom2
 
w.point(1,1) # Menggambarkan point (titik) pada koordinat x,y yaitu 1,1
w.point(2,2) # Menggambarkan point (titik) pada koordinat x,y yaitu 2,2

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan