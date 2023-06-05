from W6prak4Permut import faktorial
from W6prak5 import *

lanjut=True
while(lanjut):
    print("Silahkan Memilih Menu")
    print("1. Menghitung Faktorial")
    print("2. Menghitung luas dan keliling lingkaran")
    print("3. Menghitung pangkat")
    print("4. Menghitung Luas dan Keliling Segitiga Siku-siku")
    print("0. selesai")
    pilih=int(input("Masukkan menu --->"))
    if(pilih>4) or (pilih<0):
        lanjut = False
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif(pilih==0):
        lanjut = False
        print("Terimakasih Telah menggunakan program saya")
        break
    if(pilih==1):
        fakt=int(input("Masukkan bilangan yang di faktorialkan"))
        print("Hasil Faktorial Dari",fakt, "Adalah",faktorial(fakt))
    elif(pilih==2):
        r=int(input("Masukkan jari-jari lingkaran"))
        phi=3.14
        luasling=phi*r*r
        kelilingling=2*phi*r
        print("Luas lingkaran dengan jari-jari",r,"adalah",luasling, "cm2")
        print("Keliling lingkaran dengan jari-jari",r,"adalah",kelilingling, "cm")
    elif(pilih==3):
        print("perpangkatan")
        pangkat1
        pangkat2
        a=int(input("Masukkan bilangan yang akan dipangkatkan "))
        b=int(input("Dipangkatkan Berapa ? "))
        if(b<0):
            print("Pangkat tidak valid!")
        else:
            print("==========================================")
            print("* menggunakan loop")
            print( " " ,a,"pangkat",b,"=",pangkat1(a,b))
            print("* menggunakan recursive")
            print( " " ,a,"pangkat",b,"=",pangkat2(a,b))
            print("==========================================")
    elif(pilih==4):
        alas=int(input("Masukkan alas segitiga "))
        tinggi=int(input("Masukkan tinggi segitiga"))
        sisi=int(input("Masukkan sisi miring"))
        luassegi=0.5*alas*tinggi
        kelilingsegi=sisi+alas+tinggi
        print("Luas Segitiga adalah",luassegi, "cm2" "dan keliling segitiga adalah",kelilingsegi, "cm")
if(lanjut==True):
    print("terimakasih telah menggunakan program saya, semoga bermanfaat")
        
        


        