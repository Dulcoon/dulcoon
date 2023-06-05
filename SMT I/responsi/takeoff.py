def takeoff(jarak):
    sisa=jarak*3
    print("bensin akan berkurang sebanyak",sisa,"liter")
    return sisa

if __name__ == "__main__":
    print("anda akan melakukan penerbangan, bensin anda akan berkurang!")
    jarak=int(input("Masukkan jarak penerbangan dalam km "))
    print("sisa bensin anda adalah",takeoff(jarak))

