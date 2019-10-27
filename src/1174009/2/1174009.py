# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:56:44 2019

@author: dwiyuli
"""


# In[] : Praktikum1
import shapefile
dwi = shapefile.Writer('soal1')
dwi.shapeType
dwi.field("kolom1", "C")
dwi.field("kolom2", "C")
dwi.record("ngek", "satu")
dwi.record("ngok", "dua")
dwi.point(1, 1)
dwi.point(2, 2)
dwi.close()

# In[] : Praktikum 2
import shapefile
dwi = shapefile.Writer('soal2', shapeType=1)
dwi.shapeType
dwi.field("kolom1", "C")
dwi.field("kolom2", "C")
dwi.record("ngek", "satu")
dwi.record("ngok", "dua")
dwi.point(1, 1)
dwi.point(2, 2)
dwi.close()

# In[] : Praktikum 3
import shapefile
dwi = shapefile.Writer('soal3', shapeType=1)
dwi.shapeType
dwi.shapeType = 1
dwi.shapeType
dwi.field("kolom1", "C")
dwi.field("kolom2", "C")
dwi.record("ngek", "satu")
dwi.record("ngok", "dua")
dwi.point(1, 1)
dwi.point(2, 2)
dwi.close()


# In[] : Praktikum 4
import shapefile
dwi = shapefile.Writer('soal4', shapefile.POINT)
dwi.shapeType
dwi.field("kolom1", "C")
dwi.field("kolom2", "C")
dwi.record("ngek", "satu")
dwi.record("ngok", "dua")
dwi.point(1, 1)
dwi.point(2, 2)
dwi.close()

# In[] : Praktikum 5

import shapefile
dwi=shapefile.Writer('soal5')
dwi.shapeType
dwi.field("kolom1","C")
dwi.field("kolom2","C")
dwi.record("ngek","satu")
dwi.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
dwi.close()

# In[] : Praktikum 6
import shapefile
dwi=shapefile.Writer('soal6',shapeType=shapefile.POLYLINE)
dwi.shapeType
dwi.field("kolom1","C")
dwi.field("kolom2","C")
dwi.record("ngek","satu")
dwi.line([[[1,3],[5,3]]])
dwi.close()

# In[] : Praktikum 7
import shapefile
dwi=shapefile.Writer('soal7',shapeType=shapefile.POLYLINE)
dwi.shapeType
dwi.field("kolom1","C")
dwi.field("kolom2","C")
dwi.record("ngek","satu")
dwi.line([[[1,3],[5,3],[1,2],[5,2]]])
dwi.close()

# In[] : Praktikum 8
import shapefile
dwi=shapefile.Writer('soal8',shapeType=5)
dwi.shapeType
dwi.field("kolom1","C")
dwi.field("kolom2","C")
dwi.record("ngek","satu")
dwi.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])
dwi.close()

# In[] : Praktikum 9
import shapefile
dwi=shapefile.Writer('soal9',shapeType=shapefile.POLYGON)
dwi.shapeType
dwi.field("kolom1","C")
dwi.field("kolom2","C")
dwi.record("ngek","satu")
dwi.record("crot","dua")
dwi.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
dwi.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])
dwi.close()

# In[] : Praktikum 10
print (1174009 % 8)

import shapefile
dwi = shapefile.Writer('soal10',shapeType = 5)
dwi.shapeType
dwi.field("Kolom1","C")
dwi.field("Kolom2","C")

dwi.record("Indonesia","Merdeka")

dwi.poly([[[-4,0],[4,0],[0,5],[-4,0]]])

dwi.close()

