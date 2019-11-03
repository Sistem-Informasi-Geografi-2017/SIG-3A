# In[] Soal No 3
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal3.shp") #Digunakan untuk melakukan membaca file shp
sb = sf.bbox #Berfungsi untuk mengetahui garis tepi pada file shp tersebut
print(sb)