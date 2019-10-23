# -*- coding: utf-8 -*-
"""
Created on wed Oct 23 12:47:35 2019

@author: Sri rahayu
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor10', shapeType=5) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor10 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("C1","C") # Membuat table dengan kolom pertama
w.field("C2","C") # Membuat table dengan kolom kedua
 
w.record("Sri","Rahayu")     #Mengisi table pada kolom satu yaitu boyband dan kolom dua yaitu korea


w.poly([[[-2,1],[7,1],[7,13],[-2,1]]]) # Membuat garis dengan menghubungkan titik-titik sehingga nantinya akan membentuk sebuah bidang

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan