print("input sejumlah bilangan bulat, kemudian dipilah ganjil dan genap nya")
n1=0;n2=0;sum1=0;sum2=0
lanjut=True
while(lanjut):
    angka=int(input("masukkan bilangan bulat <isi nol untuk berhenti>"))
    if(angka==0):
        lanjut=False
        break
    if(angka%2==0):
        n2+=1
        sum2+=angka
    else:
        n1+=1
        sum1+=angka
else:
    print("inpuitan selesai")
    
# after Loop
print("anda menginputkan",n1+n2,"buah bilangan")
print("anda mendapatkan bilangan genap",n2,"buah, jumlah",sum2)
print("bilangan ganjil",n1,"buah, jumlah",sum1)