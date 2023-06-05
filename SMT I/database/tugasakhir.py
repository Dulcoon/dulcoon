import csv
from prettytable import PrettyTable
import pandas as pd
import os
from datetime import datetime
waktu_sekarang = datetime.now()
# mengatur format tanggal kedalam HH-BB-TTTT
waktu_format = waktu_sekarang.strftime("%d-%m_%Y")

data = pd.read_csv("mobil.csv")

# pemanggilan data di dalam file CSV
# kemudian disimpan ke dalam sebuah variabel
# agar mempermudah saat pemanggilan data
plat1 = data.loc[0, "Plat Nomor"]
plat2 = data.loc[1, "Plat Nomor"]
plat3 = data.loc[2, "Plat Nomor"]
plat4 = data.loc[3, "Plat Nomor"]
plat5 = data.loc[4, "Plat Nomor"]
plat6 = data.loc[5, "Plat Nomor"]
plat7 = data.loc[6, "Plat Nomor"]
plat8 = data.loc[7, "Plat Nomor"]
plat9 = data.loc[8, "Plat Nomor"]
stts1 = data.loc[0, "Status"]
stts2 = data.loc[1, "Status"]
stts3 = data.loc[2, "Status"]
stts4 = data.loc[3, "Status"]
stts5 = data.loc[4, "Status"]
stts6 = data.loc[5, "Status"]
stts7 = data.loc[6, "Status"]
stts8 = data.loc[7, "Status"]
stts9 = data.loc[8, "Status"]


# function untuk menampilkan data CSV
# dalam prettytable
def tampil_data():
    print("+------------------------[RENTAL MOBIL AYEM TENTREM]-------------------------+")
    print("Tanggal     :",waktu_format)
    print("List Mobil Yang Kami Sewakan")
    with open('mobil.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        x = PrettyTable()
        x.field_names = headers
        for row in reader:
            x.add_row(row)
        print(x)


# function program Penyewaan
def sewa():
        # memanggil function tampil data agar mempermudah user
        # dalam menginputkan data plat nomor mobil
        tampil_data()

        # menggunakan perulangan while agar saat plat mobil
        # tidak ditemukan akan diarahkan kembali ke bagian
        # penginputan plat nomor
        ulangi = True
        while ulangi == True:
            a = input("masukkan plat nomor mobil (0 untuk cancel) : ")
            if a == '0':
                os.system("cls")
                show_menu()
            # pengkondisian saat status mobil "tersedia" mobil dapat
            # disewa
            if a == plat1 and stts1 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[0, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[0, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[0, "Sewa Perhari"])

                # harga sewa perhari akan dikalikan dengan durasi sewa
                # dan disimpan dalam variabel total
                total = data.loc[0, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)

                # menggunakan perulangan while agar ketika uang yang 
                # diinputkan kurang akan langsung diarahkan untuk
                # menginputkan ualang
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        # terjadi pengubahan data agar saat penyewaan berhasil, status
                        # mobil akan berubah menjadi "tidak tersedia"
                        data.loc[0, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[0, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            # pengkondisain agar saat status mobil tidak tersedia, akan
            # muncul pesan "mobil sedang tidak ready" dan mobil tidak dapat dipesan
            elif a == plat1 and stts1 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")



            # untuk script ini akan sama mengikuti banyak nya data
            elif a == plat2 and stts2 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[1, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[1, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[1, "Sewa Perhari"])
                total = data.loc[1, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[1, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[1, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat2 and stts2 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")


            elif a == plat3 and stts3 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[2, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[2, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[2, "Sewa Perhari"])
                total = data.loc[2, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[2, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[2, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat3 and stts3 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")


            elif a == plat4 and stts4 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[3, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[3, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[3, "Sewa Perhari"])
                total = data.loc[3, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[3, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[3, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat4 and stts4 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")



            elif a == plat5 and stts5 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[4, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[4, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[4, "Sewa Perhari"])
                total = data.loc[4, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[4, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[4, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat5 and stts5 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")


            elif a == plat6 and stts6 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[5, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[5, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[5, "Sewa Perhari"])
                total = data.loc[5, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[5, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[5, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat6 and stts6 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")

            elif a == plat7 and stts7 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[6, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[6, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[6, "Sewa Perhari"])
                total = data.loc[6, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[6, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[6, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat7 and stts7 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")


            elif a == plat8 and stts8 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[7, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[7, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[7, "Sewa Perhari"])
                total = data.loc[7, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[7, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[7, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat8 and stts8 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")

            elif a == plat9 and stts9 == "Tersedia" :
                ulangi = False
                print("Mobil Tersedia")
                nama = input("masukkan Nama penyewa : ")
                no_identitas = int(input("Masukkan no identitas : "))
                hari = int(input("Masukkan Durasi penyewaan (hari) ?"))
                print(("="*20) + "[RENTAL MOBIL AYEM TENTREM]" + ("="*20))
                print("Detil Pennyewaan")
                print("Tanggal                :",waktu_format)
                print("Nama                   :",nama)
                print("No_identitas           :",no_identitas)
                print("Plat Mobil Yang disewa :", a)
                print("Merk Mobil             :" ,data.loc[8, "Merk Mobil"])
                print("Tipe Mobil             :" ,data.loc[8, "Tipe Mobil"])
                print("Hari sewa              :",hari,"hari")
                print("sewa perhari           :",data.loc[8, "Sewa Perhari"])
                total = data.loc[8, "Sewa Perhari"]*hari
                print("Total Harga Sewa Rp    :",total)
                ulang = True
                while ulang ==True:
                    up = int(input("Masukkan uang penyewa : "))
                    if up < total:
                        print("Uang kurang")
                        ulang = True
                    elif up > total:
                        kembalian = up - total
                        print("Kembalian            : Rp",kembalian,)
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press [ENTER] to Continue")
                        os.system("cls")
                        data.loc[8, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False

                    elif up == total:
                        print("Proses penyewaan berhasil")
                        print(("="*20) + "[ TERIMAKASIH ]" + ("="*20))
                        input("Press[ENTER] to Continue")
                        os.system("cls")
                        data.loc[8, "Status"] = "Tidak Tersedia"
                        data.to_csv("mobil.csv", index=False)
                        ulang = False
            elif a == plat9 and stts9 == "Tidak Tersedia" :
                ulangi = False
                print("mobil sedang tidak ready")
                input("Press [ENTER] to Continue")
                os.system("cls")
            # apabila plat yang diimputkan salah
            else:
                print("Nomor Plat Yang Diinputkan salah Silahkan Input ulang")
                ulangi = True

# function pengembalian mobil
def kembalikan():
    # memanggil function tampil data agar mempermudah user
    # dalam menginputkan data plat nomor mobil
    tampil_data()
    # menggunakan perulangan agar saat plat mobil tidak ditemukan
    # maka user akan diminta menginputkan ulang
    ulang = True
    while ulang == True:
        b = input("Masukkan plat mobil yang dikembaliakn (0 untuk batal): ")
        if b == '0':
            os.system("cls")
            show_menu()
        # pengubahan status mobil yang tadi nya tak tersedia menjadi
        # tersedia agar dapat di sewa lagi
        # script ini akan terus berulang sampai
        #  b == plat 9
        if b == plat1:
            data.loc[0, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat2:
            data.loc[1, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat3:
            data.loc[2, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat4:
            data.loc[3, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat5:
            data.loc[4, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat6:
            data.loc[5, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat7:
            data.loc[6, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat8:
            data.loc[7, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        elif b == plat9:
            data.loc[8, "Status"] = "Tersedia"
            data.to_csv("mobil.csv", index=False)
            print("pengembalian sukses")
            input("Press [ENTER} to Continue")
            os.system("cls")
            ulang = False
            show_menu()
        else:
            print("Plat tidak ditemukan")
            ulang = True



# menampilkan menu
def show_menu():
  print("="*70)
  print("Selamat datang di Aplikasi Rental Mobil")
  print("="*70)
  print("1. Sewa Mobil")
  print("2. Pengembalian Mobil")
  print("0. Keluar")
  print("---------------------------------------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("cls")

  if menu == "1":
    sewa()
  elif menu == "2":
    kembalikan()
  elif menu == "0":
    okee = str(input("Anda Yakin ingin Keluar? <y/n>"))
    if okee == 'y' or okee == 'Y':
      print("Terimakasih Telah menggunakan program saya")
      exit()
    else:
      print("Perintah keluar dibatalkan")
      input("press [ENTER] to continue")
      os.system("cls")
    # apabila menu yang diinputkan salah
  else:
    print("Menu salah!")

if __name__ == "__main__":
  while(True):
    show_menu()