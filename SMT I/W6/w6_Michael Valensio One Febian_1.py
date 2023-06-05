# NPM : 5220411200 
# Nama : Michael Valensio One Febian
# Sub Program

def greeting ():
    print("Selamat Pagi")
    print("Kita belajar function")

def perkenalan(x,y):
    print("Perkenalkan nama saya",x,"alamat di",y)
    
def hitung_gaji (a,b):
    if(b==1):
        return(a+0.3*a)
    elif(b==2):
        return(a+0.5*a)
    elif(b==3):
        return(a+0.6*a)
    elif(b==4):
        return(a+0.75*a)
    else:
        return(a)
        
    
# dipanggil
greeting()
greeting()
nama=str(input("Siapa Nama anda? "))
alamat=str(input("dimana alamat anda? "))


perkenalan(nama,alamat)
gapok=float(input("Berapa gaji pokok anda? "))
gol=int(input("pilih golongan 1-4 :"))


print("========================================================")
print("Nama        :",nama)
print("Alamat      :",alamat)
print("Gaji pokok  : Rp",gapok)
print("golongan    :",gol)
print("gaji bersih : Rp",hitung_gaji(gapok,gol))
print("========================================================")