

import shapefile #meng-import library shapefile

w = shapefile.Writer('soal8', shapeType=shapefile.POLYGON) #membuat object Writer baru dan memberi argumen berupa nama file dari shapefilenya yaitu soal8 dan argumen berupa shapeTypenya yaitu shapefile.POLYGON yang berupa poligon
w.shapeType #menentukan shapeTypenya

w.field("kolom1", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom1 dan tipe datanya yaitu char
w.field("kolom2", "C") #membuat field baru dan memberi argumen berupa nama fieldnya yaitu kolom2 dan tipe datanya yaitu char

w.record("ngek", "satu") #mengisi data pada field yang telah dibuat yaitu kolom1 = ngek dan kolom2 = satu

w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]]) #mengisi data poly sesuai koordinatnya masing-masing

w.close() #menutup file