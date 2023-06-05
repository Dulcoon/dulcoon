from takeoff import *
from isibensin import *


print("===================================")
print("Penerbangan Pesawat")
print("===================================")
bensin=400
terbang=0
lanjut=True
while(lanjut):
    print("1. Take Off")
    print("2. Periksa Bensin")
    print("3. Isi Bensin")
    print("4. Ke Bengkel")
    print("5. Bubar")
    pilih=int(input("Masukkan Pilihan ---> "))
    if(pilih>5) or (pilih<0):
        lanjut = False
        print("Pilihan yang anda pilih salah, perhatikan pilihan yang tersedia, silahkan run ulang!")
        break
    elif(pilih==1):
        if(terbang>1):
            print("Anda harus ke bengkel")
            continue
        jarak=int(input("Masukkan jarak penerbangan anda"))
        if bensin<takeoff(jarak):
            print("Bensin tidak cukup")
            continue
        bensin -= takeoff(jarak)
        print("sisa bahan bakar anda sekarang adalah",bensin)
        terbang+=1

    elif(pilih==2):
        print("sisa bahan bakar anda",bensin)
    elif(pilih==3):
        isi=int(input("Masukkan jumlah bensin yang ingin anda isi : "))
        if (bensin + isibensin(isi)>500):
            print("tangki bahan bakar tidak cukup")
            continue
        bensin += isibensin(isi)

        print("Bensin anda sekarang",bensin)

    elif(pilih==4):
        print("Pesawat anda sudah di service silahkan lakukan penerbangan ulang")
        terbang-=2
    elif(pilih==5):
        print("Terimakasih")
        break