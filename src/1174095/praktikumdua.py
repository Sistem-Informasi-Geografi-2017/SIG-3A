# In[] : Praktikum1
import shapefile
dzihan = shapefile.Writer('soal1')
dzihan.shapeType
dzihan.field("kolom1", "C")
dzihan.field("kolom2", "C")
dzihan.record("ngek", "satu")
dzihan.record("ngok", "dua")
dzihan.point(1, 1)
dzihan.point(2, 2)
dzihan.close()
# In[] : Praktikum 2
import shapefile
dzihan = shapefile.Writer('soal2', shapeType=1)
dzihan.shapeType
dzihan.field("kolom1", "C")
dzihan.field("kolom2", "C")
dzihan.record("ngek", "satu")
dzihan.record("ngok", "dua")
dzihan.point(1, 1)
dzihan.point(2, 2)
dzihan.close()

# In[] : Praktikum 3
import shapefile
dzihan = shapefile.Writer('soal3', shapeType=1)
dzihan.shapeType
dzihan.shapeType = 1
dzihan.shapeType
dzihan.field("kolom1", "C")
dzihan.field("kolom2", "C")
dzihan.record("ngek", "satu")
dzihan.record("ngok", "dua")
dzihan.point(1, 1)
dzihan.point(2, 2)
dzihan.close()


# In[] : Praktikum 4
import shapefile
dzihan = shapefile.Writer('soal4', shapefile.POINT)
dzihan.shapeType
dzihan.field("kolom1", "C")
dzihan.field("kolom2", "C")
dzihan.record("ngek", "satu")
dzihan.record("ngok", "dua")
dzihan.point(1, 1)
dzihan.point(2, 2)
dzihan.close()

# In[] : Praktikum 5

import shapefile
dzihan=shapefile.Writer('soal5')
dzihan.shapeType
dzihan.field("kolom1","C")
dzihan.field("kolom2","C")
dzihan.record("ngek","satu")
dzihan.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
dzihan.close()

# In[] : Praktikum 6
import shapefile
dzihan=shapefile.Writer('soal6',shapeType=shapefile.POLYLINE)
dzihan.shapeType
dzihan.field("kolom1","C")
dzihan.field("kolom2","C")
dzihan.record("ngek","satu")
dzihan.line([[[1,3],[5,3]]])
dzihan.close()

# In[] : Praktikum 7
import shapefile
dzihan=shapefile.Writer('soal7',shapeType=shapefile.POLYLINE)
dzihan.shapeType
dzihan.field("kolom1","C")
dzihan.field("kolom2","C")
dzihan.record("ngek","satu")
dzihan.line([[[1,3],[5,3],[1,2],[5,2]]])
dzihan.close()

# In[] : Praktikum 8
import shapefile
dzihan=shapefile.Writer('soal8',shapeType=5)
dzihan.shapeType
dzihan.field("kolom1","C")
dzihan.field("kolom2","C")
dzihan.record("ngek","satu")
dzihan.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])
dzihan.close()

# In[] : Praktikum 9
import shapefile
dzihan=shapefile.Writer('soal9',shapeType=shapefile.POLYGON)
dzihan.shapeType
dzihan.field("kolom1","C")
dzihan.field("kolom2","C")
dzihan.record("ngek","satu")
dzihan.record("crot","dua")
dzihan.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
dzihan.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])
dzihan.close()

# In[] : Praktikum 10

print(1174095 % 8)

import shapefile #mengimpor modul shapefile
w=shapefile.Writer('soal10',shapeType=shapefile.POLYGON) #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)

#mem#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bangun","C") 
w.field("Nama Bangun","C") 
 
w.record("Segitiga siku-siku","Bisma") #membuat record dengan isi kolom 1 "Segitiga siku-siku" dan kolom dua "satu"
w.record("Segitiga siku-siku","Rafael") #membuat record dengan isi kolom 2 "Segitiga siku-siku" dan kolom dua "dua"
w.record("Segitiga siku-siku","Rangga")#membuat record dengan isi kolom 3 "Segitiga siku-siku" dan kolom dua "tiga"
w.record("Segitiga siku-siku","Reza")#membuat record dengan isi kolom 4 "Segitiga siku-siku" dan kolom dua "empat"
w.record("Segitiga siku-siku","Ilham")#membuat record dengan isi kolom 5 "Segitiga siku-siku" dan kolom dua "lima"
w.record("Segitiga siku-siku","udin")
w.record("Segitiga siku-siku","dede")
w.record("Segitiga siku-siku","didin")
w.record("Segitiga siku-siku","asep")
w.record("Segitiga siku-siku","asup")
#membuat 5 row karena menggunakan 5 record
w.poly([[[1,1],[5,1], [1,5],[1,1]]]) #membuat polygon
w.poly([[[1,-1],[5,-1],[1,-5],[1,-1]]])  #membuat polygon
w.poly([[[-1,-1],[-5,-1],[-1,-5],[-1,-1]]])  #membuat polygon
w.poly([[[-1,1],[-5,1],[-1,5],[-1,1]]])  #membuat polygon
w.poly([[[2,5],[6,5],[6,1],[2,5]]])  #membuat polygon
w.poly([[[2,-5],[6,-5],[6,-1],[2,-5]]])
w.poly([[[-2,-5],[-6,-5],[-6,-1],[-2,-5]]])
w.poly([[[-2,5],[-6,5],[-6,1],[-2,5]]])
w.poly([[[2,-5],[6,-5],[6,-1],[2,-5]]])
w.poly([[[5,6],[5,6],[-5,10],[5,6]]])
w.close()#melakukan save dengan nama (soal10)

#%%
