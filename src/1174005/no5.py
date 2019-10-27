# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:11:44 2019

@author: ONIWALDUS
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor5', shapeType=3) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor5 dan bentuknya itu adalah shapetype 3 yaitu PolyLine (Garis)

w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua
 
w.record("ngek","satu") # Mengisi untuk table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan
