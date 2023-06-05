# NPM : 5220411200 
# Nama : Michael Valensio One Febian
# Rekursive

def pangkat1(x,y):
    pang=1
    for i in range (1,y+1):
        pang=pang*x
    return pang

def pangkat2(x,y):
    if(y==0):
        return 1
    else:
        return(x*pangkat2(x,y-1))

if __name__ == "__main__":
    print("menghitung angka")
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