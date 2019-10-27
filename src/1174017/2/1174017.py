# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:36:52 2019

@author: Rifky
"""


# In[] : Praktikum1
import shapefile
rifky = shapefile.Writer('soal1')
rifky.shapeType
rifky.field("kolom1", "C")
rifky.field("kolom2", "C")
rifky.record("ngek", "satu")
rifky.record("ngok", "dua")
rifky.point(1, 1)
rifky.point(2, 2)
rifky.close()

# In[] : Praktikum 2
import shapefile
rifky = shapefile.Writer('soal2', shapeType=1)
rifky.shapeType
rifky.field("kolom1", "C")
rifky.field("kolom2", "C")
rifky.record("ngek", "satu")
rifky.record("ngok", "dua")
rifky.point(1, 1)
rifky.point(2, 2)
rifky.close()

# In[] : Praktikum 3
import shapefile
rifky = shapefile.Writer('soal3', shapeType=1)
rifky.shapeType
rifky.shapeType = 1
rifky.shapeType
rifky.field("kolom1", "C")
rifky.field("kolom2", "C")
rifky.record("ngek", "satu")
rifky.record("ngok", "dua")
rifky.point(1, 1)
rifky.point(2, 2)
rifky.close()


# In[] : Praktikum 4
import shapefile
rifky = shapefile.Writer('soal4', shapefile.POINT)
rifky.shapeType
rifky.field("kolom1", "C")
rifky.field("kolom2", "C")
rifky.record("ngek", "satu")
rifky.record("ngok", "dua")
rifky.point(1, 1)
rifky.point(2, 2)
rifky.close()

# In[] : Praktikum 5

import shapefile
rifky=shapefile.Writer('soal5')
rifky.shapeType
rifky.field("kolom1","C")
rifky.field("kolom2","C")
rifky.record("ngek","satu")
rifky.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
rifky.close()

# In[] : Praktikum 6
import shapefile
rifky=shapefile.Writer('soal6',shapeType=shapefile.POLYLINE)
rifky.shapeType
rifky.field("kolom1","C")
rifky.field("kolom2","C")
rifky.record("ngek","satu")
rifky.line([[[1,3],[5,3]]])
rifky.close()

# In[] : Praktikum 7
import shapefile
rifky=shapefile.Writer('soal7',shapeType=shapefile.POLYLINE)
rifky.shapeType
rifky.field("kolom1","C")
rifky.field("kolom2","C")
rifky.record("ngek","satu")
rifky.line([[[1,3],[5,3],[1,2],[5,2]]])
rifky.close()

# In[] : Praktikum 8
import shapefile
rifky=shapefile.Writer('soal8',shapeType=5)
rifky.shapeType
rifky.field("kolom1","C")
rifky.field("kolom2","C")
rifky.record("ngek","satu")
rifky.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])
rifky.close()

# In[] : Praktikum 9
import shapefile
rifky=shapefile.Writer('soal9',shapeType=shapefile.POLYGON)
rifky.shapeType
rifky.field("kolom1","C")
rifky.field("kolom2","C")
rifky.record("ngek","satu")
rifky.record("crot","dua")
rifky.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
rifky.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])
rifky.close()

# In[] : Praktikum 10
print (1174017 % 8)

import shapefile
rifky = shapefile.Writer('soal10',shapeType = 5)
rifky.shapeType
rifky.field("Kolom1","C")
rifky.field("Kolom2","C")

rifky.record("Indonesia","Merdeka")

rifky.poly([[[-4,0],[4,0],[0,5],[-4,0]]])

rifky.close()
