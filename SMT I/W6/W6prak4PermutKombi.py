# NPM : 5220411200 
# Nama : Michael Valensio One Febian
# Recursive

def faktorial(x):
    if(x==0):
        return 1
    else:
        return(x*faktorial(x-1))

print("Menghitung Faktorial, Permutasi, dan Kombinasi")
a=int(input("Masukkan bilangan yg di faktorialkan "))
if (a<0):
    print("Bil. tdk valid")
else:
    print(a,"faktorial =" ,faktorial(a))
print("Permutasi & Kombinasi")
a=int(input("Masukkan jmlh bil."))
b=int(input("pengelompokkan bil."))
if(a<b):
    print("Permutasi Komb Tidak bisa dilakukkan")
else:
    print("Hasil permutasi dari",a,"dan",b,"=",faktorial(a)/(faktorial(a-b)))
    print("Hasil permutasi dari",a,"dan",b,"=",faktorial(a)/(faktorial(a-b)*faktorial(b)))