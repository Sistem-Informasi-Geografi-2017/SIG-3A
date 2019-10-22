# In[] : Praktikum1
import shapefile
harun = shapefile.Writer('soal1')
harun.shapeType
harun.field("kolom1", "C")
harun.field("kolom2", "C")
harun.record("ngek", "satu")
harun.record("ngok", "dua")
harun.point(1, 1)
harun.point(2, 2)
harun.close()
# In[] : Praktikum 2
import shapefile
harun = shapefile.Writer('soal2', shapeType=1)
harun.shapeType
harun.field("kolom1", "C")
harun.field("kolom2", "C")
harun.record("ngek", "satu")
harun.record("ngok", "dua")
harun.point(1, 1)
harun.point(2, 2)
harun.close()

# In[] : Praktikum 3
import shapefile
harun = shapefile.Writer('soal3', shapeType=1)
harun.shapeType
harun.shapeType = 1
harun.shapeType
harun.field("kolom1", "C")
harun.field("kolom2", "C")
harun.record("ngek", "satu")
harun.record("ngok", "dua")
harun.point(1, 1)
harun.point(2, 2)
harun.close()


# In[] : Praktikum 4
import shapefile
harun = shapefile.Writer('soal4', shapefile.POINT)
harun.shapeType
harun.field("kolom1", "C")
harun.field("kolom2", "C")
harun.record("ngek", "satu")
harun.record("ngok", "dua")
harun.point(1, 1)
harun.point(2, 2)
harun.close()

# In[] : Praktikum 5

import shapefile
harun=shapefile.Writer('soal5')
harun.shapeType
harun.field("kolom1","C")
harun.field("kolom2","C")
harun.record("ngek","satu")
harun.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
harun.close()

# In[] : Praktikum 6
import shapefile
harun=shapefile.Writer('soal6',shapeType=shapefile.POLYLINE)
harun.shapeType
harun.field("kolom1","C")
harun.field("kolom2","C")
harun.record("ngek","satu")
harun.line([[[1,3],[5,3]]])
harun.close()

# In[] : Praktikum 7
import shapefile
harun=shapefile.Writer('soal7',shapeType=shapefile.POLYLINE)
harun.shapeType
harun.field("kolom1","C")
harun.field("kolom2","C")
harun.record("ngek","satu")
harun.line([[[1,3],[5,3],[1,2],[5,2]]])
harun.close()

# In[] : Praktikum 8
import shapefile
harun=shapefile.Writer('soal8',shapeType=5)
harun.shapeType
harun.field("kolom1","C")
harun.field("kolom2","C")
harun.record("ngek","satu")
harun.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])
harun.close()

# In[] : Praktikum 9
import shapefile
harun=shapefile.Writer('soal9',shapeType=shapefile.POLYGON)
harun.shapeType
harun.field("kolom1","C")
harun.field("kolom2","C")
harun.record("ngek","satu")
harun.record("crot","dua")
harun.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
harun.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])
harun.close()

# In[] : Praktikum 10

print(1174027 % 8)

import shapefile

harun = shapefile.Writer('soal10',shapeType = 5)
harun.shapeType
harun.field("Kolom1","C")
harun.field("Kolom2","C")

harun.record("Guardian","Dragon")
harun.record("Star","Galaxy")

harun.poly([[[1,5],[5,5],[5,6],[1,6],[1,5]]])
harun.poly([[[1,8],[5,8],[5,7],[1,7],[1,8]]])

harun.close()

#%%
