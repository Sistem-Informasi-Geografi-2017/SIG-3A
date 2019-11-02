# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:58:22 2019

@author: Damara
"""
# In[Soal 1]
import shapefile 
sf = shapefile.Reader("soal1")
print(sf)
# In[Soal 2]
import shapefile 
sf = shapefile.Reader("soal1") 
sf.shapeType 
# In[Soal 3]
import shapefile 
sf = shapefile.Reader("soal1") 
sf.bbox 
# In[Soal 4]
import shapefile 
sf = shapefile.Reader("soal1") 
anu=sf.shapes()
len(anu) 
# In[Soal 5]
import shapefile 
sf = shapefile.Reader("soal1") 
anu=sf.shapes() 
dir(anu) 
dir(anu[0]) 
# In[Soal 6]
import shapefile 
sf = shapefile.Reader("soal7")
anu=sf.shapes() 
anu[0].shapeType 
# In[Soal 7]
import shapefile 
sf = shapefile.Reader("soal7") 
anu=sf.shapes() 
anu[0].parts 
# In[Soal 8]
import shapefile 
sf = shapefile.Reader("soal7") 
anu=sf.shapes() 
anu[0].points 
# In[Soal 9]
import shapefile 
sf = shapefile.Reader("soal7") 
namakolom = sf.fields
print(namakolom) 
# In[Soal 10]
import shapefile 
sf = shapefile.Reader("soal7") 
isidata = sf.records() 
print(isidata)
# In[Soal 11]
import shapefile 
sf = shapefile.Reader("soal7") 
isidata = sf.records() 
print(isidata[0]) 
print(isidata[0][0]) 

