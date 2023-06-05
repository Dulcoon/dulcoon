# Nama : Michael Valensio One Febian
# NIM : 5220411200
# Mendeteksi status kesehatan seseorang

Nama=str(input("Masukkan Nama Anda :"))
TD=int(input("Masukkan Tekanan darah anda :"))
statusTD_normal=True
if(TD>300):
    statusTD_normal=False
    stts=("hipertensi akut")
elif(TD in range (150, 300)):
    statusTD_normal=False
    stts=("hipertensi ringan")
elif(TD in range (100, 150)):
    statusTD_normal=True
    stts=("tekanan darah normal")
elif(TD<100):
    statusTD_normal=False
    stts=("hipotensi")

    
    
GD=int(input("Masukkan Kadar Gula Darah Anda :"))
if(GD>300):
    statusGD_normal=False
    stts2=("diabet")
elif(GD in range (120, 300)):
    statusGD_normal=False
    stts2=("Waspada Diabet")
elif(GD<120):
    statusGD_normal=True
    stts2=("Normal")
    
# after
print("Nama Pasien :" ,Nama)
print("Masukkan Tekanan darah :" ,TD)
print("Masukkan Tekanan Gula darah :" ,GD)

print("===================================")
# data
print(Nama)
print("Status1 (tekanan Darah) :" ,stts )
print("Status2 (tekanan Gula Darah) :" ,stts2 )
if(statusTD_normal==True) and (statusGD_normal==True):
    print("Status3 (Keseluruhan) : Anda Normal")
else:
    print("Status3 (Keseluruhan) : Anda kurang sehat")
    


    



    