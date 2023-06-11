# Muhammad Rossi Pratama
# 5220411200

import os

class Node:
    def __init__(self, noSku, namaBarang, hargaSatuan, jumlahStok):
        self.noSku = noSku
        self.namaBarang = namaBarang
        self.hargaSatuan = hargaSatuan
        self.jumlahStok = jumlahStok
        self.left = None
        self.right = None


transaksi_konsumen = []


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def restok_barang(self):
        SKU = int(input("Masukkan No.SKU : "))
        temp = self.root
        while (temp is not None):
            if SKU < temp.noSku:
                temp = temp.left
            elif SKU > temp.noSku:
                temp = temp.right
            else:
                stokBaru = int(input("Masukkan Stok Baru : "))
                temp.jumlahStok += stokBaru
                print("Stok Berhasil Ditambahkan!")
                break
        else:
            print("No.SKU Belum Terdaftar!")
            print("Silahkan Melakukan Input Data Stok Barang Terlebih Dahulu.")
            ask = input("Ingin Melakukan Transaksi Lagi (y/n) : ")
            if ask == "y":
                self.restok_barang()
            else:
                return False

    def kelola_transaksi_konsumen(self):
        nama = input("Masukkan Nama Konsumen : ")
        ulang = False

        while not ulang:
            temp = self.root 
            SKU = int(input("Masukkan No.SKU : "))
            tersedia = False
            while temp is not None and not ulang:
                if SKU < temp.noSku:
                    temp = temp.left
                elif SKU > temp.noSku:
                    temp = temp.right
                else:
                    tersedia = True
                    inputUlang = True
                    while inputUlang:
                        jumlah = int(input("Masukkan Jumlah Beli: "))
                        if temp.jumlahStok >= jumlah:
                            transaksi_konsumen.append({
                                "nama Konsumen": nama,
                                "nama barang" : temp.namaBarang,
                                "SKU": SKU,
                                "jumlah": jumlah,
                                "subtotal": jumlah * temp.hargaSatuan
                            })
                            temp.jumlahStok -= jumlah
                            print("Transaksi Berhasil")
                            inputUlang = False
                            ulang = True
                        else:
                            print("Stok Tidak Cukup")
                            ask = input("Ingin Melanjutkan Transaksi? (y/n) : ")
                            if ask == "y":
                                inputUlang = True
                            else:
                                inputUlang = False
                                ulang = True

            if not tersedia:
                print("No.SKU Belum Terdaftar!")
                ask = input("Ingin Melanjutkan Transaksi? (y/n) : ")
                if ask == "n":
                    ulang = True
        
    def input_data_barang(self):
        SKU = int(input("Masukkan No.SKU (Int Only) : "))
        if self.root is None:
            namaBarang = input("Masukkan Nama Barang : ")
            hargaSatuan = int(input("Masukkan Harga Satuan : "))
            jumlahStok = int(input("Masukkan Jumlah Stok Barang : "))
            self.root = Node(SKU, namaBarang, hargaSatuan, jumlahStok)
            return True
        temp = self.root
        while (True):
            if SKU == temp.noSku:
                print("No SKU sudah Terdaftar")
                return False
            if SKU < temp.noSku:
                if temp.left is None:
                    namaBarang = input("Masukkan Nama Barang : ")
                    hargaSatuan = int(input("Masukkan Harga Satuan : "))
                    jumlahStok = int(input("Masukkan Jumlah Stok Barang : "))
                    temp.left = Node(SKU, namaBarang, hargaSatuan, jumlahStok)
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    namaBarang = input("Masukkan Nama Barang : ")
                    hargaSatuan = int(input("Masukkan Harga Satuan : "))
                    jumlahStok = int(input("Masukkan Jumlah Stok Barang : "))
                    temp.right = Node(SKU, namaBarang, hargaSatuan, jumlahStok)
                    return True
                temp = temp.right

    def data_transaksi(self):
        print("")
        print("{:<15} {:<15} {:<10} {:<10} {:<15}".format(
            "Nama Konsumen", "Nama Barang", "SKU", "Jumlah", "Subtotal (Rp)"
        ))
        
        for transaksi in transaksi_konsumen:
            nama_konsumen = transaksi["nama Konsumen"]
            nama_barang = transaksi["nama barang"]
            sku = transaksi["SKU"]
            jumlah = transaksi["jumlah"]
            subtotal = transaksi["subtotal"]
            
            print("{:<15} {:<15} {:<10} {:<10} {:<15}".format(
                nama_konsumen, nama_barang, sku, jumlah, subtotal
            ))
        print("")
        
    def data_transaksi_urut(self):
        sorted_data = self.insertion_sort(transaksi_konsumen, key=lambda x: x["subtotal"])
        print("")
        print("{:<15} {:<15} {:<10} {:<10} {:<15}".format(
            "Nama Konsumen", "Nama Barang", "SKU", "Jumlah", "Subtotal (Rp)"
        ))
        
        for transaksi in sorted_data:
            nama_konsumen = transaksi["nama Konsumen"]
            nama_barang = transaksi["nama barang"]
            sku = transaksi["SKU"]
            jumlah = transaksi["jumlah"]
            subtotal = transaksi["subtotal"]
            
            print("{:<15} {:<15} {:<10} {:<10} {:<15}".format(
                nama_konsumen, nama_barang, sku, jumlah, subtotal
            ))
        print("")
        

    def insertion_sort(self,my_list, key=lambda x: x):
        for i in range(1, len(my_list)):
            temp = my_list[i]
            j = i - 1
            while j >= 0 and key(temp) > key(my_list[j]):
                my_list[j + 1] = my_list[j]
                j -= 1
            my_list[j + 1] = temp
        return my_list


    def insertDummy(self, noSku, namaBarang, hargaSatuan, jumlahStok):
            new_node = Node(noSku, namaBarang, hargaSatuan, jumlahStok)
            if self.root is None:
                self.root = new_node
                return True
            temp = self.root
            while (True):
                if new_node.noSku == temp.noSku:
                    return False
                if new_node.noSku < temp.noSku:
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
        print("===========Pengelola Stok Barang dan Transaksi=============")
        print("1) Kelola Stok Barang")
        print("2) Kelola Transaksi Konsumen")
        print("3) Exit")
        print("===========================================================")
        pilih = input("Masukkan Menu >> ")
        if pilih == "1":
            while True:
                os.system("cls")
                print("**Kelola Stok Barang**")
                print("1) Input data stok barang")
                print("2) Restok barang")
                print("3) Kembali Ke Menu Utama")
                pilihh = input("Masukkan Menu : ")
                if pilihh == "1":
                    print("Input data barang")
                    myTree.input_data_barang()
                elif pilihh == "2":
                    print("Restok Barang")
                    myTree.restok_barang()
                elif pilihh == "3":
                    menu()
                else:
                    print("menu salah")
                    continue
                os.system("pause")

        elif pilih == "2":
            while True:
                os.system("cls")
                print("**Kelola Transaksi**")
                print("1) Input Data Transaksi Baru")
                print("2) Lihat Data Seluruh Transaksi Konsumen")
                print("3) Data Transaksi Urut Berdasarkan Subtotal")
                print("4) Back")
                menuu = input("Masukkan Menu : ")
                if menuu == "1":
                    myTree.kelola_transaksi_konsumen()
                elif menuu == "2":
                    myTree.data_transaksi()
                elif menuu == "3":
                    myTree.data_transaksi_urut()
                elif menuu == "4":
                    menu()
                else:
                    print("menu salah")
                    continue
                os.system("pause")
        else:
            print("Terimakasih!")
            exit()
if __name__=="__main__":
    menu()