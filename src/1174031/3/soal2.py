# In[] Soal No 2
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal2.shp") #Digunakan untuk melakukan membaca file shp
st= sf.shapeType #Untuk mengetahui Type dari file SHP yang dibaca
print(st)