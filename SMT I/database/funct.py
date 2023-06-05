def kasir():
    print("Kamu sudah stop dan masuk ke fungsi kasir")

lanjut_beli = 1

while lanjut_beli > 0:
    print(" ========================================")
    print("Selamat Datang di Aneka Jajanan Pasar")
    print("List Makanan")
    print(" ========================================")
    print("1. Martabak kari         @10.000")
    print("2. Hamburger             @10.000")
    print("3. Bubur Sum-sum         @5.000")
    print("4. Bubur Kacang Hijau    @5.000")
    print("5. Pudding               @5.000")
    print("6. Roti Sosis            @5.0000")
    print("7. Hot Pangsit           @3.000")
    print("8. Bakwan                @2.000")
    print("9. Risol                 @2.000")
    print("10. Donat                @2.000")
    print("11. Bayar")
    print(" ========================================")

    nomor = int(input("Masukkan angka sesuai list menu yang tersedia: "))
    jumlah = int(input("Masukkan jumlah pembelian:"))
    if nomor == 1:
        nama_menu = "Martabak Kari"
        harga = int(10000 * jumlah)
    elif nomor == 2:
        nama_menu = "Hamburger"
        harga = int(10000 * jumlah)
    elif nomor == 3:
        nama_menu = "Bubur Sum-sum "
        harga = int(5000 * jumlah)
    elif nomor == 4:
        nama_menu = "Bubur Kacang Hijau"
        harga = int(5000 * jumlah)
    elif nomor == 5:
        nama_menu = "Pudding"
        harga = int(5000 * jumlah)
    elif nomor == 6:
        nama_menu = "Roti Sosis"
        harga = int(5000 * jumlah)
    elif nomor == 7:
        nama_menu = "Hot Pangsit"
        harga = int(3000 * jumlah)
    elif nomor == 8:
        nama_menu = "Bakwan"
        harga = int(2000 * jumlah)
    elif nomor == 9:
        nama_menu = "Risol"
        harga = int(2000 * jumlah)
    elif nomor == 10:
        nama_menu = "Donat"
        harga = int(2000 * jumlah)
    elif nomor == 11:
        lanjut_beli = 0
    else:
        print("Maaf, menu yang Anda pilih tidak tersedia.")
        lanjut_beli = input("Ingin membeli lagi? <y/n>")
        if lanjut_beli == "n" or lanjut_beli == "N" :
            lanjut_beli = 0
        else:
            lanjut_beli = 1

kasir()