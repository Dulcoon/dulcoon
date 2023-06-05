def faktorial(x):
    if(x==0):
        return 1
    else:
        return(x*faktorial(x-1))


if __name__ == "__main__":
    a=int(input("Masukkan bilangan yg di faktorialkan "))
    if (a<0):
        print("Bil. tdk valid")
    else:
        print(a,"faktorial =" ,faktorial(a))
