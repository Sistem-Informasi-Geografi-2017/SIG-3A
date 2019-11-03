# In[] Soal No 4
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal4.shp") #Digunakan untuk melakukan membaca file shp
sp=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
print(len(sp))