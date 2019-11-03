
print(1174021 % 8)

import shapefile #meng-import library shapefile

w = shapefile.Writer('soal10', shapeType=5) #membuat object Writer baru dan memberi argumen berupa nama file dari shapefilenya yaitu soal10 dan argumen berupa shapeTypenya yaitu shapefile.POLYGON yang berupa poligon
w.shapeType #menentukan shapeTypenya

w.field("kolom1", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom1 dan tipe datanya yaitu char
w.field("kolom2", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom2 dan tipe datanya yaitu char

w.record("ngok", "ngek")
w.record("ngak", "ngik") #mengisi data pada field yang telah dibuat yaitu kolom1 = ngok dan kolom2 = ngek

w.poly([[[7,3],[11,6],[7,9],[3,6]]])
w.poly([[[-7,-3],[-11,-6],[-7,-9],[-3,-6]]])  #mengisi data poly sesuai koordinatnya masing-masing

w.close() #menutup file