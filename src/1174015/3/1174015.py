# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:13:56 2019

@author: USER
"""

# In[] : praktikum1
import shapefile 
sf = shapefile.Reader("soal1")
print(sf) #menampilkan apa yang telah dipanggil pada variabel sf
# In[] : praktikum2
import shapefile 
sf = shapefile.Reader("soal1") 
sf.shapeType #Untuk mengetahui Type dari file SHP yang dibaca
# In[] : praktikum3
import shapefile 
sf = shapefile.Reader("soal2") 
sf.bbox #Berfungsi untuk mengetahui garis tepi pada file shp tersebut
# In[] : praktikum4
import shapefile 
sf = shapefile.Reader("soal2") 
anu=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut 
len(anu) #digunakan untuk menampilkan jumlah data dari file shp tersebut
# In[] : praktikum5
import shapefile 
sf = shapefile.Reader("soal2") 
anu=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
dir(anu) #Digunakan mengetahui object yang digunakan
dir(anu[0]) #Digunakan untuk mengetahui object yang digunakan berdasarkan nomber index 0
# In[] : praktikum6
import shapefile 
sf = shapefile.Reader("soal7") 
anu=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
anu[0].shapeType #Digunakan untuk membaca shape type yang digunakan pada index ke 0
# In[] : praktikum7
import shapefile 
sf = shapefile.Reader("soal8") 
anu=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
anu[0].parts #Jika sebuah bentuk terbentuk dari kumpulan beberapa point maka akan mengembalikan 0,
#JIka hanya point, tapi tidak terbentuk sesuatu maka akan mengembalikan array kosong
# In[] : praktikum8
import shapefile 
sf = shapefile.Reader("soal8") 
anu=sf.shapes(0) #Digunakan untuk membaca jumlah data yang ada di file shp tersebut dan index ke 0
anu.points #Menampilkan Koordinat yang ada pada baris tersebut
# In[] : praktikum9
import shapefile 
sf = shapefile.Reader("soal8") 
namakolom = sf.fields #Digunakan untuk membca field yang ada pada file SHP Tersebut 
print(namakolom) # Digunakan Untuk menampilkan field tersebut
# In[] : praktikum10
import shapefile 
sf = shapefile.Reader("soal8") 
isidata = sf.records() #membaca seluruh data yang ada di dalam file shp tersebut 
print(isidata)
# In[] Soal 11
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
isidata = sf.records() #membaca seluruh data yang ada di dalam file shp tersebut
print(isidata[0]) #menampilkan data pada index ke 0
print(isidata[0][0]) #menampilkan data pada index ke 0 dan urutan ke 0