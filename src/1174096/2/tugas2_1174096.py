# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:56:09 2019

@author: Nico Sembiring
"""

# In[] : Praktikum1
import shapefile
w = shapefile.Writer('soal1')
w.shapeType
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.record("ngok", "dua")
w.point(1, 1)
w.point(2, 2)
w.close()
# In[] : Praktikum 2
import shapefile
w = shapefile.Writer('soal2', shapeType=1)
w.shapeType
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.record("ngok", "dua")
w.point(1, 1)
w.point(2, 2)
w.close()

# In[] : Praktikum 3
import shapefile
w = shapefile.Writer('soal3', shapeType=1)
w.shapeType
w.shapeType = 1
w.shapeType
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.record("ngok", "dua")
w.point(1, 1)
w.point(2, 2)
w.close()


# In[] : Praktikum 4
import shapefile
w = shapefile.Writer('soal4', shapefile.POINT)
w.shapeType
w.field("kolom1", "C")
w.field("kolom2", "C")
w.record("ngek", "satu")
w.record("ngok", "dua")
w.point(1, 1)
w.point(2, 2)
w.close()

# In[] : Praktikum 5

import shapefile
w=shapefile.Writer('soal5')
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.close()

# In[] : Praktikum 6
import shapefile
w=shapefile.Writer('soal6',shapeType=shapefile.POLYLINE)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.line([[[1,3],[5,3]]])
w.close()

# In[] : Praktikum 7
import shapefile
w=shapefile.Writer('soal7',shapeType=shapefile.POLYLINE)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.line([[[1,3],[5,3],[1,2],[5,2]]])
w.close()

# In[] : Praktikum 8
import shapefile
w=shapefile.Writer('soal8',shapeType=5)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])
w.close()

# In[] : Praktikum 9
import shapefile
w=shapefile.Writer('soal9',shapeType=shapefile.POLYGON)
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("ngek","satu")
w.record("crot","dua")
w.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
w.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])
w.close()

# In[] : Praktikum 10

print(1174096 % 8)
import shapefile
w = shapefile.Writer('soal10',shapeType = 5)
w.shapeType
w.field("Kolom1","C")
w.field("Kolom2","C")
w.record("zeus","satu") 
w.record("poseidon","dua") 
w.record("hades","tiga")
w.record("hestia","empat")
w.record("hera","lima") 
w.record("ares","enam") 
w.record("athena","tujuh") 
w.record("apollo","delapan") 
w.record("aphrodite","sembilan") 
w.poly([[[1,1],[5,1],[3,5],[1,1]]]) 
w.poly([[[5,5],[7,1],[9,5],[5,5]]])
w.poly([[[9,1],[13,1],[11,5],[9,1]]])
w.poly([[[13,5],[15,1],[17,5],[13,5]]])
w.poly([[[17,1],[21,1],[19,5],[17,1]]])
w.poly([[[5,7],[9,7],[7,11],[5,7]]])
w.poly([[[9,11],[11,7],[13,11],[9,11]]])
w.poly([[[13,7],[17,7],[15,11],[13,7]]])
w.poly([[[9,13],[13,13],[11,17],[9,13]]])
w.close()