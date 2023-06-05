from array import *

list_buah= ["mangga","jeruk","apel","anggur","semangka","rambutan","kelengkeng","sawo"]
while(True):
    print("Silahkan Memilih Menu")
    print("1. Cetak list buah")
    print("2. Tambah elemen")
    print("3. Edit data di list")
    print("4. Menghapus data di dalam list")
    print("5. Mengurutkan data di dalam list")
    print("6. Karakter terbanyak")
    print("7. Karakter tersedikit")
    print("0. selesai")
    pilih=int(input("Masukkan menu --->"))
    if(pilih>7) or (pilih<0):
        lanjut = False
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif(pilih==0):
        lanjut = False
        print("Terimakasih Telah menggunakan program saya")
        break
    if(pilih==1):
        x=len(list_buah)
        for i in range (x):
            print("data ke",i,"  ",list_buah[i])
    elif(pilih==2):
        print("Tambah data")
        index=int(input("Index ke berapa? "))
        i=str(input("Masukkan data baru : "))
        list_buah.insert(index, i)
        print(list_buah) 
    elif(pilih==3):
        print("Update nilai di list")
        i=int(input("Ubah data ke berapa? "))
        if i<0 or i>len(list_buah):
            print("Index yang dimasukkan salah")
            continue
        print("Data ke ",i,"Adalah",list_buah[i])
        list_buah[i]=str(input("Masukkan data yamh baru : "))
        print(list_buah)
    elif(pilih==4):
        print("Menghapus data di list")
        i=int(input("Hapus data ke berapa? "))
        print("Data ke ",i,"Adalah",list_buah[i])
        y=str(input("Anda yakin ingin menghapu data? (y/n)"))
        if y=="y":
            del list_buah[i]
            print("Data sudah dihapus")
            print(list_buah)
        elif y=="n":
            continue
    elif(pilih==5):
        print("Data telah diurutkan berdasarkan abjad")
        list_buah.sort()
        print(list_buah)
        x=len(list_buah)
        for i in range (x):
            print("data ke",i,"  ",list_buah[i])
    elif(pilih==6):
        print("karatkter terbanyak")
        terpanjang = ''
        for x in list_buah :
            if len(x) > len(terpanjang) :
                terpanjang = x
        print(terpanjang)
    elif(pilih==7):
        print("karatkter tersedikit")
        terpendek = ''
        for x in list_buah :
            if len(x) < len(terpendek) :
                terpendek = x
        print(terpendek)
        

