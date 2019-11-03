# In[] Soal No 7
import shapefile #mengimport shapefile
sf = shapefile.Reader("soal6.shp") #membaca file shp yang bernama Soal6.shp
sp = sf.shapes() # membaca shapes 
anu = sp[0].parts #untuk membaca ada berapa part yg ada..jika hanya ada satu maka dikembalikan nilai 0
print(anu) #menampilkan isi dari variable anu