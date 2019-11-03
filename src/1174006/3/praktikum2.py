# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:45:02 2019

@author: vanerz
"""

# In[1]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
print(sf) #menampilkan isi object sf

# In[2]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
sf.shapeType #mengetahui tipe shape dari file shp atau dbf

# In[3]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
sf.bbox #mengetahui koordinat shape dari file shp

# In[4]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
anu=sf.shapes() #mendapatkan list koordinat dan ditampung pada anu
len(anu) #membaca jumlah data dari file shp

# In[5]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
anu=sf.shapes() #mendapatkan list koordinat dan ditampung pada anu
dir(anu) #mengetahui object yang digunakan pada anu
dir(anu[0]) #mengetahui object yang digunakan pada anu index 0

# In[6]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
anu=sf.shapes() #mendapatkan list koordinat dan ditampung pada anu
anu[0].shapeType #mengetahui tipe shape yang digunakan pada anu index 0

# In[7]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
anu=sf.shapes() #mendapatkan list koordinat dan ditampung pada anu
anu[0].parts #menampilkan list pada anu index 0

# In[8]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
anu=sf.shapes() #mendapatkan list koordinat dan ditampung pada anu
anu[0].points #mengetahui koordinat pada anu index 0

# In[9]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
namakolom= sf.fields #mendapatkan field pada file shp dan ditampung pada namakolom
print(namakolom) #menampilkan isi namakolom

# In[10]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
isidata= sf.records() #mendapatkan data pada file shp dan ditampung pada isidata
print(isidata) #menampilkan isi isidata

# In[11]

import shapefile #mengimport library bernama shapefile
sf = shapefile.Reader("../2/soal1") #membuat object Reader bernama sf dengan argumen nama file shp atau dbf
isidata = sf.records() #mendapatkan data pada file shp dan ditampung pada isidata
print(isidata[0]) #menampilkan isi isidata pada index 0
print(isidata[0][0]) #menampilkan isi isidata pada index 0 dan data ke 0