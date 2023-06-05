print("prmggunaan loop for")
print("mencetak vilangan genap antara a dan b")
a=int(input("masukkan awal loop :"))    
b=int(input("masukkan akhir loop :"))    
sum=0;n=0
if(a<b):
    for i in range(a,b+1):
        if(i==0):
            continue
        if(i%2==0):
            print(i," ",end="")
            sum+=1
            n+=1
else:
    for i in range(a,b-1,-1):
        if(i==0):
            continue
        if(i%2==0):
            print(i," ",end="")
            sum+=1
            n+=1
            
# after loop
if(n>0):
    print("\nAnda mencetak",n,"buah bilangan genap")
    print("jumlah bilangan tersebut =",sum)
    print("Rata-ratanya =",sum/n)
    print("terimakasih")
else:
    print("tidak ada bilangan yang dicetak")
print("terimakasih")