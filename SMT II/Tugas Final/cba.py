import os
import pyinputplus as pyip
from prettytable import PrettyTable
table = PrettyTable()

dataTransaksi = []

class Node:
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
        SKU = pyip.inputNum("Masukkan No.SKU : ", min=1000, max=9999)
        temp = self.root
        while (temp is not None):
            if SKU < temp.SKU:
                temp = temp.left
            elif SKU > temp.SKU:
                temp = temp.right
            else:
                stokBaru = pyip.inputNum("Masukkan Stok Baru : ")
                temp.jumlahStok += stokBaru
                print("Stok Berhasil Ditambahkan!")
                break
        else:
            print("No.SKU Belum Terdaftar, \nSilahkan Melakukan Input Data Stok Barang Terlebih Dahulu!")
            ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
            if ask.lower() == "y":
                self.restok()
            else:
                return False
            
    def hapusStok(self):
        SKU = pyip.inputNum("Masukkan No.SKU : ", min=1000, max=9999)
        temp = self.root
        while (temp is not None):
            if SKU < temp.SKU:
                temp = temp.left
            elif SKU > temp.SKU:
                temp = temp.right
            else:
                stokBaru = pyip.inputNum("Masukkan Jumlah Stok Yang Akan Dikurangi : ")
                if stokBaru > temp.jumlahStok:
                    print("Jumlah Stok Yang Diinputkan Tidak Valid")
                    break
                else:
                    temp.jumlahStok -= stokBaru
                    print("Stok Berhasil Dikurangkan!")
                    break
        else:
            print("No.SKU Belum Terdaftar, \nSilahkan Melakukan Input Data Stok Barang Terlebih Dahulu!")
            ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
            if ask.lower() == "y":
                self.restok()
            else:
                return False

    def kelolaTransaksi(self):
        nama = input("Masukkan Nama Konsumen : ")
        loop_selesai = False
        while not loop_selesai:
            temp = self.root 
            SKU = pyip.inputNum("Masukkan No.SKU : ", min=1000, max=9999)
            barang_ditemukan = False
            while temp is not None and not loop_selesai:
                if SKU < temp.SKU:
                    temp = temp.left
                elif SKU > temp.SKU:
                    temp = temp.right
                else:
                    barang_ditemukan = True
                    inputUlang = True
                    print("========== Detil Barang ==========")
                    print("Nama Barang : ", temp.namaBarang)
                    print("Harga Satuan Barang : Rp",temp.hargaSatuan) 
                    print("Jumlah Stok : ", temp.jumlahStok) 
                    print("==================================")
                    while inputUlang:
                        jumlah = pyip.inputNum("Masukkan Jumlah Beli: ")
                        if temp.jumlahStok >= jumlah:
                            dataTransaksi.append({
                                "nama Konsumen": nama,
                                "nama barang" : temp.namaBarang,
                                "SKU": SKU,
                                "jumlah": jumlah,
                                "subtotal": jumlah * temp.hargaSatuan
                            })
                            temp.jumlahStok -= jumlah
                            print("Transaksi Berhasil")
                            inputUlang = False
                            loop_selesai = True
                        else:
                            print("Stok Tidak Mencukupi")
                            ask = input("Apakah Anda Ingin Melanjutkan Transaksi? (y/n) : ")
                            if ask.lower() == "y":
                                inputUlang = True
                            else:
                                inputUlang = False
                                loop_selesai = True

            if not barang_ditemukan:
                print("No.SKU Belum Terdaftar!")
                ask = input("Apakah Anda Ingin Melanjutkan Transaksi? (y/n) : ")
                if ask.lower() == "n":
                    loop_selesai = True

   
        
    def insert(self):
        SKU = pyip.inputNum("Masukkan No.SKU (Int Only) : ", min=1000, max=9999)
        if self.root is None:
            namaBarang = input("Masukkan Nama Barang : ")
            hargaSatuan = pyip.inputInt("Masukkan Harga Satuan : ")
            jumlahStok = pyip.inputInt("Masukkan Jumlah Stok Barang : ")
            self.root = Node(SKU, namaBarang, hargaSatuan, jumlahStok)
            return True
        temp = self.root
        while (True):
            if SKU == temp.SKU:
                print("No SKU sudah Terdaftar")
                return False
            if SKU < temp.SKU:
                if temp.left is None:
                    namaBarang = input("Masukkan Nama Barang : ")
                    hargaSatuan = pyip.inputInt("Masukkan Harga Satuan : ")
                    jumlahStok = pyip.inputInt("Masukkan Jumlah Stok Barang : ")
                    temp.left = Node(SKU, namaBarang, hargaSatuan, jumlahStok)
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    namaBarang = input("Masukkan Nama Barang : ")
                    hargaSatuan = pyip.inputInt("Masukkan Harga Satuan : ")
                    jumlahStok = pyip.inputInt("Masukkan Jumlah Stok Barang : ")
                    temp.right = Node(SKU, namaBarang, hargaSatuan, jumlahStok)
                    return True
                temp = temp.right

    def printDataBarang(self):
        table = PrettyTable()
        table.field_names = ["No.SKU", "Nama Barang", "Harga Satuan (Rp)", "Sisa Stok"]
        self.printTabel(self.root, table)
        print(table)

    def printTabel(self, node, table):
        if node is not None:
            self.printTabel(node.left, table)
            table.add_row([node.SKU, node.namaBarang, node.hargaSatuan, node.jumlahStok])
            self.printTabel(node.right,table)

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
            while j >= 0 and key(temp) > key(my_list[j]):  # Ubah tanda < menjadi >
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


    def insertDummy(self, SKU, namaBarang, hargaSatuan, jumlahStok):
            new_node = Node(SKU, namaBarang, hargaSatuan, jumlahStok)
            if self.root is None:
                self.root = new_node
                return True
            temp = self.root
            while (True):
                if new_node.SKU == temp.SKU:
                    return False
                if new_node.SKU < temp.SKU:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right
myTree = BinarySearchTree()
myTree.insertDummy(3333, "udud", 20000, 33)
myTree.insertDummy(4444, "rokok", 20000, 33)
myTree.insertDummy(5555, "baju", 20000, 33)
myTree.insertDummy(6666, "celana", 20000, 33)
def menu():
    os.system("cls")
    while True:
        print("===========SISTEM INFORMASI STOK DAN TRANSAKSI=============")
        print("1) Kelola Stok Barang")
        print("2) Kelola Transaksi Konsumen")
        print("3) Exit")
        print("===========================================================")
        pilih = input("Masukkan Menu >> ")
        if pilih == "1":
            while True:
                os.system("cls")
                print("MENU KELOLA STOK BARANG")
                print("a) Input data stok barang")
                print("b) Restok barang")
                print("c) Hapus stok barang (Barang Expired)")
                print("d) Lihat Data Barang")
                print("e) Kembali Ke Menu Utama")
                pilihh = input("Masukkan Menu (a/b/c/d) >> ")
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
                    menu()
                else:
                    print("menu salah")
                    continue
                input("Press [ENTER] To Continue...")

        elif pilih == "2":
            while True:
                os.system("cls")
                print("MENU KELOLA TRANSAKSI KONSUMEN")
                print("a) Input Data Transaksi Baru")
                print("b) Lihat Data Seluruh Transaksi Konsumen")
                print("c) Lihat Data Transaksi Berdasarkan Subtotal")
                print("d) Kembali Ke Menu Utama")
                pilih2 = input("Masukkan Menu (a/b/c/d) >> ")
                if pilih2.lower() == "a":
                    myTree.kelolaTransaksi()
                elif pilih2.lower() == "b":
                    myTree.printDataTransaksi()
                elif pilih2.lower() == "c":
                    myTree.printDataTransaksiSorted()
                elif pilih2.lower() == "d":
                    menu()
                else:
                    print("menu salah")
                    continue
                input("Press [ENTER] To Continue...")
        elif pilih == "3":
            print("Terimakasih Telah Menggunakan Program Saya!")
            exit()
if __name__=="__main__":
    menu()
