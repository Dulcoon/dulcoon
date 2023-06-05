import csv
import datetime
 
waktu = datetime.datetime.now()
def waktu_sekarang() :
    listTime = []
    listTime.append(waktu.day)
    listTime.append(waktu.month)
    listTime.append(waktu.year)
    return str(listTime[0])+"-"+str(listTime[1])+"-"+str(listTime[2])
 
plat = []
merk = []
tipe = []
sewa = []
def data_csv(a,b,c,d) :
    data = "car.csv"
    with open(data,"r") as fileName :
        csvdata = csv.reader(fileName)
        for row in csvdata :
            a.append(row[0])
            b.append(row[1])
            c.append(row[2])
            d.append(row[3])
    return a,b,c,d
 
data_csv(plat,merk,tipe,sewa)
# print(plat)
 
def rent_a_car(index) :
    penyewa = input("Nama Penyewa       :")
    NIM__Id = int(input("Nomor Identitas    :"))
    rentTime= int(input("Lama Sewa          :"))
    tot_sewa = rentTime * int(sewa[index])
    print("total biaya sewa   :",tot_sewa)
    print("""
+----------------------------[Terima Kasih]-----------------------------+    
    """)
    exit()
    
 
if __name__ =="__main__" :
    print(f"""
+----------------------[RENTAL MOBIL AYEM TENTREM]----------------------+
Tanggal :          {waktu_sekarang()}
Daftar Mobil Tersedia :
+--------+--------+--------+--------+--------+--------+--------+--------+
|    Plat Nomor   |    Merk Mobil   |    Tipe Mobil   |    Sewa Perhari |
+--------+--------+--------+--------+--------+--------+--------+--------+
|     AB0101CE    |     Toyota      |    Yaris G-CV   |     250000      |
|     AA1424DW    |     Toyota      |    Hilux D Cap  |     430000      |
|     AB4590QE    |     Suzuki      |      Karimun    |     220000      |
|     AD90057AC   |     Daihatsu    |      Terios     |     300000      |
+--------+--------+--------+--------+--------+--------+--------+--------+
    """)
    rental = True
    while rental == True :
        print("Silahkan isi data penyewaan : ")
        cekPlat = input("Plat nomor         :")
        if cekPlat == plat[1] :
            i = 1
            rent_a_car(i)
            rental = False
        elif cekPlat == plat[2] :
            i = 2
            rent_a_car(i)
            rental = False
        elif cekPlat == plat[3] :
            i = 3
            rent_a_car(i)
            rental = False
        elif cekPlat == plat[4] :
            i = 4
            rent_a_car(i)
            rental = False
        else :
            print("Nomor Plat tidak ditemukan,masukkan dengan benar\n")
            rental = True
rent_a_car(index=1)
