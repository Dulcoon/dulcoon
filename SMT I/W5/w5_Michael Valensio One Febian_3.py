print("segitiga bilangan ganjil genap")
n=int(input("Berapa baris bilangan yang akan dicetak? "))
# segitiga ganjil
for i in range (1,n+1):
    a=1
    for j in range (1,i+1):
        print(a," ",end="")
        a+=2
    print()
# segitiga genap
for i in range (n,0,-1):
    a=2
    for j in range (1,i+1):
        print(a," ",end="")
        a+=2
    print()