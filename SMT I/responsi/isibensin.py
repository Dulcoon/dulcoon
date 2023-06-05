def isibensin(x):
    b=13000
    jmlh=x//b
    return jmlh

if __name__ == "__main__":
    l=int(input("Masukkan jmlh beli"))
    print(isibensin(l))
