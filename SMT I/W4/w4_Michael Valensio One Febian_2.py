# Berhak BLT atau tidak
Nama=str(input("Masukkan Nama Anda :"))
umur=int(input("Masukkan Umur Anda :"))
status_blt=False
if(umur<18):
    ss=int(input("Pilih status sekolah 1. Sekolah 0. tdk sekolah"))
    if(ss==0):
        status_blt=True
    else:
        status_blt=False
else: #  blok yang usia>18
    sb=int(input("Pilih Pekerjaan 1. Bekerja 0. Tidak bekerja"))
    if(sb==0):
        status_blt=True
    else:
        income=float(input("Masukkan jumlah penghasilan Rp :"))
        tg=int(input("Jumlah tanggungan :"))
        rasio=income/tg
        if(rasio>300000):
            status_blt=False
        else:
            status_blt=True
# after if
# mencetak hasil
print("Nama    :" ,Nama)
print("Umur    :" ,umur)
print("Umur    :" ,umur)
if(status_blt==True):
    print("Anda berhak dapat BLT Maszeeee")
else:
    print("Maaf anda belum beruntung")
    
print("Sekian terimagaji")
