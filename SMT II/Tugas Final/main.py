# Michael Valensio One Febian
# 5220411200

import os
from prettytable import PrettyTable
import matplotlib.pyplot as plt
table = PrettyTable()


dataTransaksi = []

def inputSku(prompt):
    while True:
        try:
            ipt = int(input(prompt))
        except ValueError:
            print("Input harus berupa int!")
            ipt = None
            continue
        if ipt > 9999 or ipt < 1000:
            print("No SKU harus terdiri dari 4 digit angka!")
            continue
        return ipt
    
def inputInt(prompt):
    while True:
        try:
            ipt = int(input(prompt))
        except ValueError:
            print("Input harus berupa int!")
            ipt = None
            continue
        return ipt

class barang:
    def __init__(self, SKU, namaBarang, hargaSatuan, jumlahStok):
        self.SKU = SKU
        self.namaBarang = namaBarang
        self.hargaSatuan = hargaSatuan
        self.jumlahStok = jumlahStok
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def restok(self):
        SKU = inputSku("Masukkan No.SKU : ")
        temp = self.contains(SKU)
        if temp is not None:
                stokBaru = inputInt("Masukkan Stok Baru : ")
                temp.jumlahStok += stokBaru
                print("Stok Berhasil Ditambahkan!")
        else:
            print("No.SKU Belum Terdaftar, \nSilahkan Melakukan Input Data Stok Barang Terlebih Dahulu!")
            ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
            if ask.lower() == "y":
                self.restok()

            

    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.SKU:
                temp = temp.left
            elif value > temp.SKU:
                temp = temp.right
            else:
                return temp
        return None
    

    def hapusStok(self):
        SKU = inputSku("Masukkan No.SKU : ")
        temp = self.contains(SKU)
        if temp is not None:
                stokBaru = inputInt("Masukkan Jumlah Stok Yang Akan Dikurangi : ")
                if stokBaru > temp.jumlahStok:
                    print("Input Anda melebihi Jumlah Stok Saat ini!")
                else:
                    temp.jumlahStok -= stokBaru
                    print("Stok Berhasil Dikurangkan!")
                    ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
                    if ask.lower() == "y":
                        self.hapusStok()
        else:
            print("No.SKU Belum Terdaftar!")
            ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
            if ask.lower() == "y":
                self.hapusStok()

    def kelolaTransaksi(self):
        nama = input("Masukkan Nama :")
        ulang = True
        while ulang == True:
            sku = inputSku("Masukkan No SKU : ")
            temp = self.contains(sku)
            if temp is not None:
                print("========== Detil Barang ==========")
                print("Nama Barang              : ", temp.namaBarang)
                print("Harga Satuan Barang (Rp) : ",temp.hargaSatuan) 
                print("Jumlah Stok              : ", temp.jumlahStok) 
                print("==================================")
                while True:
                    jumlah = inputInt("Masukkan jumlah beli     :  ")
                    if jumlah <= temp.jumlahStok:
                            temp.jumlahStok -= jumlah
                            dataTransaksi.append({
                                "nama Konsumen": nama,
                                "nama barang" : temp.namaBarang,
                                "SKU": sku,
                                "jumlah": jumlah,
                                "subtotal": jumlah * temp.hargaSatuan
                            })
                            print("Subtotal (Rp)            : ", jumlah * temp.hargaSatuan) 
                            print("==================================")
                            print("Data Transaksi Berhasil Diinputkan!")
                            lagi = input("Apakah ingin menambahkan data pembelian untuk konsumen ini (y/n)")
                            if lagi.lower() == "y":
                                break
                            else:
                                ulang = False
                                break
                    print("Stok Barang Tidak Mencukupi!")
                    tanya = input("apakah ingin melanjutkan transaksi ? (y/n)")
                    if tanya.lower() == "y":
                        break
                    else:
                        ulang = False
                        break
            else:
                print("SKU belum terdaftar")
                tanya = input("apakah ingin melanjutkan transaksi ? (y/n)")
                if tanya.lower() == "y":
                    continue
                else:
                    break

    def inputInsert(self):
        namaBarang = input("Masukkan Nama Barang : ")
        hargaSatuan = inputInt("Masukkan Harga Satuan : ")
        jumlahStok = inputInt("Masukkan Jumlah Stok Barang : ")
        return namaBarang, hargaSatuan, jumlahStok
    
    def insert(self):
        SKU = inputSku("Masukkan No.SKU : ")
        if self.root is None:
            namaBarang, hargaSatuan, jumlahStok = self.inputInsert()
            self.root = barang(SKU, namaBarang, hargaSatuan, jumlahStok)
            print("Input Data Stok Barang Berhasil")
            return True
        temp = self.root
        while True:
            if SKU == temp.SKU:
                print("No SKU sudah Terdaftar! Permintaan Input Data Ditolak")
                return False
            if SKU < temp.SKU:
                if temp.left is None:
                    namaBarang, hargaSatuan, jumlahStok = self.inputInsert()
                    temp.left = barang(SKU, namaBarang, hargaSatuan, jumlahStok)
                    print("Input Data Stok Barang Berhasil")
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    namaBarang, hargaSatuan, jumlahStok = self.inputInsert()
                    temp.right = barang(SKU, namaBarang, hargaSatuan, jumlahStok)
                    print("Input Data Stok Barang Berhasil")
                    return True
                temp = temp.right

    def cariBarangBySKU(self):
        SKU = inputSku("Masukkan No.SKU yang ingin dicari: ")
        temp = self.contains(SKU)
        if temp is not None:
            table = PrettyTable()
            table.field_names = ["No.SKU", "Nama Barang", "Harga Satuan (Rp)", "Sisa Stok"]
            self.printTabelCariBarang(temp, table)
            print(table)
        else:
            print("Barang dengan No.SKU tersebut tidak ditemukan.")

    def printTabelCariBarang(self, barang, table):
        if barang is not None:
            table.add_row([barang.SKU, barang.namaBarang, barang.hargaSatuan, barang.jumlahStok])

    def printDataBarang(self):
        table = PrettyTable()
        table.field_names = ["No.SKU", "Nama Barang", "Harga Satuan (Rp)", "Sisa Stok"]
        self.printTabel(self.root, table)
        print(table)

    def printTabel(self, barang, table):
        if barang is not None:
            self.printTabel(barang.left, table)
            table.add_row([barang.SKU, barang.namaBarang, barang.hargaSatuan, barang.jumlahStok])
            self.printTabel(barang.right,table)

    def printDataTransaksi(self):
        table = PrettyTable()
        table.field_names = ["Nama Konsumen", "Nama Barang", "SKU", "Jumlah", "Subtotal (Rp)"]
        for transaksi in dataTransaksi:
            table.add_row([transaksi["nama Konsumen"], transaksi["nama barang"], transaksi["SKU"], transaksi["jumlah"], transaksi["subtotal"]])
        print(table)

    def insertion_sort(self,my_list, key=lambda x: x):
        for i in range(1, len(my_list)):
            temp = my_list[i]
            j = i - 1
            while j >= 0 and key(temp) > key(my_list[j]):
                my_list[j + 1] = my_list[j]
                j -= 1
            my_list[j + 1] = temp
        return my_list
    
    def printDataTransaksiSorted(self):
        sorted_data = self.insertion_sort(dataTransaksi, key=lambda x: x["subtotal"])
        table = PrettyTable()
        table.field_names = ["Nama Konsumen", "Nama Barang", "SKU", "Jumlah", "Subtotal (Rp)"]
        for transaksi in sorted_data:
            table.add_row([transaksi["nama Konsumen"], transaksi["nama barang"], transaksi["SKU"], transaksi["jumlah"], transaksi["subtotal"]])
        print(table)



    def printGrafikPenjualan(self):
        penjualan = {}
        for transaksi in dataTransaksi:
            namaBarang = transaksi["nama barang"]
            jumlah = transaksi["jumlah"]
            if namaBarang in penjualan:
                penjualan[namaBarang] += jumlah
            else:
                penjualan[namaBarang] = jumlah

        plt.bar(penjualan.keys(), penjualan.values())
        plt.xlabel("Nama Barang")
        plt.ylabel("Jumlah Total Penjualan")
        plt.title("Grafik Penjualan Barang")
        plt.xticks(rotation=45)

        for i, v in enumerate(penjualan.values()):
            plt.text(i, v, str(v), ha='center', va='bottom')

        plt.show()



    def insertDummy(self, SKU, namaBarang, hargaSatuan, jumlahStok):
            new_barang = barang(SKU, namaBarang, hargaSatuan, jumlahStok)
            if self.root is None:
                self.root = new_barang
                return True
            temp = self.root
            while (True):
                if new_barang.SKU == temp.SKU:
                    return False
                if new_barang.SKU < temp.SKU:
                    if temp.left is None:
                        temp.left = new_barang
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_barang
                        return True
                    temp = temp.right
myTree = BinarySearchTree()
myTree.insertDummy(3333, "Beras", 60000, 33)
myTree.insertDummy(4444, "Rokok", 20000, 45)
myTree.insertDummy(5555, "baju", 20000, 33)
myTree.insertDummy(6666, "celana", 20000, 33)
def menu():
    os.system("cls")
    while True:
        print("\n===========SISTEM INFORMASI STOK DAN TRANSAKSI=============")
        print("1) Kelola Stok Barang")
        print("2) Kelola Transaksi Konsumen")
        print("3) Exit")
        print("===========================================================")
        pilih = input("Masukkan Menu >> ")
        if pilih == "1":
            while True:
                os.system("cls")
                print("\nMENU KELOLA STOK BARANG")
                print("a) Input data stok barang")
                print("b) Restok barang")
                print("c) Hapus stok barang")
                print("d) Lihat Data Barang")
                print("e) Cari Barang Dengan SKU")
                print("f) Kembali Ke Menu Utama")
                pilihh = input("Masukkan Menu (a/b/c/d/e/f) >> ")
                if pilihh.lower() == "a":
                    myTree.insert()
                elif pilihh.lower() == "b":
                    print("MENU RESTOK BARANG")
                    myTree.restok()
                elif pilihh.lower() == "c":
                    print("MENU HAPUS STOK BARANG")
                    myTree.hapusStok()
                elif pilihh.lower() == "d":
                    myTree.printDataBarang()
                elif pilihh.lower() == "e":
                    myTree.cariBarangBySKU()
                elif pilihh.lower() == "f":
                    menu()
                else:
                    print("menu salah")
                    continue
                input("Press [ENTER] To Continue...")

        elif pilih == "2":
            while True:
                os.system("cls")
                print("\nMENU KELOLA TRANSAKSI KONSUMEN")
                print("a) Input Data Transaksi Baru")
                print("b) Lihat Data Seluruh Transaksi Konsumen")
                print("c) Lihat Data Transaksi Berdasarkan Subtotal")
                print("d) Lihat Grafik Penjualan")
                print("e) Kembali Ke Menu Utama")
                pilih2 = input("Masukkan Menu (a/b/c/d/e) >> ")
                if pilih2.lower() == "a":
                    myTree.kelolaTransaksi()
                elif pilih2.lower() == "b":
                    myTree.printDataTransaksi()
                elif pilih2.lower() == "c":
                    myTree.printDataTransaksiSorted()
                elif pilih2.lower() == "d":
                    myTree.printGrafikPenjualan()
                elif pilih2.lower() == "e":
                    menu()
                else:
                    print("menu salah")
                    continue
                input("Press [ENTER] To Continue...")
        else:
            print("Terimakasih Telah Menggunakan Program Saya!")
            break
if __name__=="__main__":
    menu()
