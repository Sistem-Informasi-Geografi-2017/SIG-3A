import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
print(sf) #menampilkan apa yang telah dipanggil pada variabel sf
# In[] No 2
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
sf.shapeType #Untuk mengetahui Type dari file SHP yang dibaca
# In[] No 3
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
sf.bbox #Berfungsi untuk mengetahui garis tepi pada file shp tersebut
# In[] No 4
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
anu=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
len(anu) #digunakan untuk menampilkan jumlah data dari file shp tersebut
# In[] Soal 5
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
anu=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
dir(anu) #Digunakan mengetahui object yang digunakan
dir(anu[0]) #Digunakan untuk mengetahui object yang digunakan berdasarkan nomber index 0
# In[] Soal 6
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
anu=sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
anu[0].shapeType #Digunakan untuk membaca shape type yang digunakan pada index ke 0
# In[] Soal 7
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
s = sf.shapes() #Digunakan untuk membaca jumlah data yang ada di file shp tersebut
s[0].parts
#Jika sebuah bentuk terbentuk dari kumpulan beberapa point maka akan mengembalikan 0,
#JIka hanya point, tapi tidak terbentuk sesuatu maka akan mengembalikan array kosong

# In[] Soal 8
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
anu=sf.shape(0) #Digunakan untuk membaca jumlah data yang ada di file shp tersebut dan index ke 0
anu.points #Menampilkan Koordinat yang ada pada baris tersebut
# In[] Soal 9
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
namakolom = sf.fields #Digunakan untuk membca field yang ada pada file SHP Tersebut
print(namakolom) # Digunakan Untuk menampilkan field tersebut
# In[] Soal 10
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
isidata = sf.records() #membaca seluruh data yang ada di dalam file shp tersebut
print(isidata) #menampilkan data tersebut
# In[] Soal 11
import shapefile #Digunakan untuk memanngil library SHP
sf = shapefile.Reader("soal1") #Digunakan untuk melakukan membaca file shp
isidata = sf.records() #membaca seluruh data yang ada di dalam file shp tersebut
print(isidata[0]) #menampilkan data pada index ke 0
print(isidata[0][0]) #menampilkan data pada index ke 0 dan urutan ke 0