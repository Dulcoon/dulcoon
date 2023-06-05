import datetime
now = datetime.datetime.now()
import os


buku=dict(
    Judul= "",
    Penulis= "",
    Harga= 0,
    Jumlah_Halaman=0,
    uang=0,
    kembalian=0
)

def isi_data_buku():
    a = str(input("Masukkan Judul buku : "))
    buku["Judul"]=a
    b = str(input("Masukkan Penulis buku : "))
    buku["Penulis"]=b
    c = int(input("Masukkan Harga Buku : "))
    buku["Harga"]=c
    d = int(input("Masukkan Jumlah halaman Buku : "))
    buku["Jumlah_Halaman"]=d
    print("data buku berhasil diinputkan!")
def ubah_judul_buku():
    judulBaru = str(input("Masukkan Judul baru : "))
    buku["Judul"]=judulBaru
    print("Judul Berhasil diubah!")
def hapus_buku():
    x=str(input("Apakah Anda yakin ingin menghapus buku ?(y/n)"))
    if x=="y":
        buku.clear
        print("Buku berhasil dihapus")
    else:
        print("Buku tidak jadi dihapus")
def transaksi():
    print("Jual Beli")
    uang=int(input("Masukan Uang anda: "))
    if uang<buku["Harga"]:
        print("Uang anda kurang")
    else:
        print("==========S T R U K==========")  
        print("--Judul Buku :",buku["Judul"])  
        print("--Penulis    :",buku["Penulis"])  
        print("--Harga      :",buku["Harga"])  
        print("--uang anda  :",uang) 
        if uang>buku["Harga"]:
            kembalian=uang-buku["Harga"]
            print("--Kembalian = ",kembalian)
        print("==========T E R I M A K A S I H==========")  


        
    
        
while True:
    print("1. Isi data buku : ")
    print("2. Cetak buku : ")
    print("3. Ubah judul buku : ")
    print("4. Hapus Buku : ")
    print("5. Beli Buku : ")
    print("0. Keluar : ")
    menu = int(input("Masukkan Menu : "))
    if(menu>5) or (menu<0):
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif menu == 1:
       isi_data_buku()
    elif menu == 2:
        for key in buku:
            print(key, "->", buku[key])
        print("TimeStamp : ",now)
    elif menu == 3:
        ubah_judul_buku()
        print("TimeStamp : ",now)
    elif menu == 4:
        hapus_buku()
        print("Data buku berhasil dihapus.")
        print("TimeStamp : ",now)
    elif menu == 5:
        transaksi()
        print("TimeStamp : ",now)
    else:
        print("Terimakasih telah  menggunakan program saya")
        break
    os.system("pause")
        
