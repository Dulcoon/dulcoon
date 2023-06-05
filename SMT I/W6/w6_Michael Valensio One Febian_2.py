from w6Valen import *



print("Konversi KiloMeter ke satuan panjang lainnya.")
lanjut=True
km=float(input("masukkan panjang dalam km :"))
while(lanjut):
    print("Silahkan Memilih Menu")
    print("1. Konversi km ke hm")
    print("2. Konversi km ke dam")
    print("3. Konversi km ke m")
    print("4. Konversi km ke dm")
    print("5. Konversi km ke cm")
    print("6. Konversi km ke mm")
    print("0. selesai")
    pilih=int(input("Masukkan menu --->"))
    if(pilih>6) or (pilih<0):
        lanjut = False
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif(pilih==0):
        lanjut = False
        break
    if(pilih==1):   
        # hm=km*10
        print("Hasil konversi ke hm adalah :",hm(km),"hm")
    elif(pilih==2): 
        # dam=km*100
        print("Hasil konversi ke dam adalah :",dam(km),"dam")
    elif(pilih==3): 
        # m=km*1000
        print("Hasil konversi ke m adalah :",m(km),"m")
    elif(pilih==4): 
        # dm=km*10000
        print("Hasil konversi ke dm adalah :",dm(km),"dm")
    elif(pilih==5): 
        # cm=km*100000
        print("Hasil konversi ke cm adalah :",cm(km),"cm")
    elif(pilih==6): 
        # mm=km*1000000
        print("Hasil konversi ke mm adalah :",mm(km),"mm")
# after while
if(lanjut==True):
    print("terimakasih telah menggunakan program saya, semoga bermanfaat")