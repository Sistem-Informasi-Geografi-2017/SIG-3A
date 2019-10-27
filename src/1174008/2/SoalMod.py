import shapefile #mengimport shapefile
w=shapefile.Writer('SoalMod', shapeType=shapefile.POLYGON) #membuat file bernama SoalMod dan mendifinisikan shapetypenya yaitu POLYGON
w.shapeType #mendeklarasikan(memanggil) shape type
w.field("kolom1","C") #membuat field pertama 
w.field("kolom2","C") #membuat field kedua
w.record("ngek","satu") #membuat record pertama
w.record("baaa","dua") #membuat record kedua
w.record("bii","tiga") #membuat record ketiga
w.record("buu","empat") #membuat record keempat
w.record("aa","satu") #membuat record kelima
w.record("bb","dua") #membuat record keenam
w.record("cc","tiga") #membuat record ketujuh
w.record("dd","empat") #membuat record kedelapan
w.poly([[[2,7],[4,7],[3,10],[3,10],[2,7]]]) #memmbuat polygon pertama
w.poly([[[2,3],[4,3],[3,6],[3,6],[2,3]]]) #memmbuat polygon kedua
w.poly([[[5,3],[7,3],[6,6],[6,6],[5,3]]]) #memmbuat polygon ketiga
w.poly([[[5,7],[7,7],[6,10],[6,10],[5,7]]]) #memmbuat polygon keempat
w.poly([[[8,7],[10,7],[9,10],[9,10],[8,7]]]) #membuat polygon kelima
w.poly([[[8,3],[10,3],[9,6],[9,6],[8,3]]]) #membuat polygon keenam
w.poly([[[11,3],[13,3],[12,6],[12,6],[11,3]]]) #membuat polygon ketujuh
w.poly([[[11,7],[13,7],[12,10],[12,10],[11,7]]]) #membuat polygon kedelapan
w.close()  #menghentikan perintah