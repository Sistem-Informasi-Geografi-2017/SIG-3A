# In[] Soal No 6
import shapefile #mengimport shapefile
sf = shapefile.Reader("soal6.shp") #membaca file shp yang bernama Soal6.shp
sp = sf.shapes() # membaca shapes nya
anu = sp[0].shapeType # membaca shape type dari sp index 0
print(anu) # menampilkan isi dari variable anu