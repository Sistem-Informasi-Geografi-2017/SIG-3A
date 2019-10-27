# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:11:51 2019

@author: ONIWALDUS
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor6', shapeType=5) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor6 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua
 
w.record("ngek","satu") # Mengisi untuk table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2

w.poly([[[1,3],[5,3]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan 
