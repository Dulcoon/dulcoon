import os
from prettytable import PrettyTable
table = PrettyTable()

dataTransaksi = []

class Node:
    def __init__(self, SKU, nama_barang, harga_satuan, jumlah_stok):
        self.SKU = SKU
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, SKU, nama_barang, harga_satuan, jumlah_stok):
        self.root = self._insert_recursive(self.root, SKU, nama_barang, harga_satuan, jumlah_stok)

    def _insert_recursive(self, node, SKU, nama_barang, harga_satuan, jumlah_stok):
        if node is None:
            return Node(SKU, nama_barang, harga_satuan, jumlah_stok)
        if SKU < node.SKU:
            node.left = self._insert_recursive(node.left, SKU, nama_barang, harga_satuan, jumlah_stok)
        else:
            node.right = self._insert_recursive(node.right, SKU, nama_barang, harga_satuan, jumlah_stok)
        return node

    def restok(self, SKU, jumlah_stok_baru):
        self._restok_recursive(self.root, SKU, jumlah_stok_baru)

    def _restok_recursive(self, node, SKU, jumlah_stok_baru):
        if node is None:
            print("No. SKU yang diinputkan belum terdaftar.")
            os.system('pause')
            os.system('cls')
            return
        if node.SKU == SKU:
            node.jumlah_stok += jumlah_stok_baru
            print("Data stok barang berhasil di restok")
            os.system('pause')
            os.system('cls')
            return
        if SKU < node.SKU:
            self._restok_recursive(node.left, SKU, jumlah_stok_baru)
        else:
            self._restok_recursive(node.right, SKU, jumlah_stok_baru)

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
    
# SUB MENU UTAMA NOMOR 1
    def input_barang(self):
        SKU = int(input("Masukkan SKU barang (INTEGER ONLY): "))
        if self.contains(SKU) is not None:
            print("No. SKU sudah terdaftar ! silahkan input dengan Nomor yang berbeda.")
            return False
        
        nama_barang = input("Masukkan nama barang: ")
        harga_satuan = float(input("Masukkan harga satuan barang: "))
        jumlah_stok = int(input("Masukkan jumlah stok barang: "))
        self.insert(SKU, nama_barang, harga_satuan, jumlah_stok)
        print("Data stok barang berhasil diinput.")



    def restok_barang(self):
        SKU = int(input("Masukkan SKU barang yang akan direstok: "))
        Node = self.contains(SKU)
        if Node is None:
            print("No. SKU tidak ada / terdaftar")
            os.system('pause')
            os.system('cls')
            return 
        else :
            jumlah_stok_baru = int(input("Masukkan jumlah stok baru: "))
            self.restok(SKU, jumlah_stok_baru)
            print("Barang berhasil di restok")
        
    def lihat_ketersediaanBarang(self):
        print("\n=== KETERSEDIAAN BARANG ===")
        if self.root is None:
            print("Belum ada data stok barang.")

        else:
            table = PrettyTable()
            table.field_names = ["No. SKU barang", "Nama barang", "Harga satuan (Rp)", "Sisa stok"]

            stack = []
            current = self.root

            while True:
                if current is not None:
                    stack.append(current)
                    current = current.left
                elif stack:
                    current = stack.pop()
                    table.add_row([current.SKU, current.nama_barang, current.harga_satuan, current.jumlah_stok])
                    current = current.right
                else:
                    break
            print(table)
    
# SUB MENU UTAMA NOMOR 2
    def input_transaksi(self):
        nama_konsumen = input("Masukkan nama konsumen: ")
        while True:
            SKU = int(input("Masukkan SKU barang yang dibeli: "))
            item = self.contains(SKU)
            if item is None:
                print("No. SKU yang diinputkan belum terdaftar.")
                choice = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
                if choice.lower() == "y":
                    # self.input_transaksi()
                    continue
                else:
                    break
            print("\n=== DETAIL BARANG ===")
            print("No. SKU barang:", item.SKU)
            print("Nama barang:", item.nama_barang)
            print("Harga satuan:", item.harga_satuan)
            print("Jumlah stok:", item.jumlah_stok)

            jumlah_beli = int(input("Masukkan jumlah barang yang dibeli: "))

            if item.jumlah_stok >= jumlah_beli:
                subtotal = item.harga_satuan * jumlah_beli
                item.jumlah_stok -= jumlah_beli
                dataTransaksi.append({
                    "Nama Konsumen": nama_konsumen,
                    "Nama Barang": item.nama_barang,
                    "No. SKU": SKU,
                    "Jumlah Beli": jumlah_beli,
                    "Subtotal": subtotal
                })
                print("Data transaksi konsumen berhasil diinput.")
                choice = input("Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)? ")
                if choice.lower() == "y":
                    # self.input_transaksi()
                    continue
                else:
                    break
            else:
                print("Jumlah Stok No. SKU yang Anda beli tidak mencukupi.")
                choice = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
                if choice.lower() == "y":
                    # self.input_transaksi()
                    continue

    

    def lihat_transaksi_konsumen(self):
        print("\n=== DATA SELURUH TRANSAKSI KONSUMEN ===")
        if len(dataTransaksi) == 0:
            print("Belum ada transaksi.")
        else:
            table = PrettyTable()
            table.field_names = ["Nama Konsumen", "Nama Barang", "No. SKU", "Jumlah Beli", "Subtotal"]
        
        for transaction in dataTransaksi:
            nama_konsumen = transaction["Nama Konsumen"]
            nama_barang = transaction["Nama Barang"]
            no_sku_barang = transaction["No. SKU"]
            jumlah_beli = transaction["Jumlah Beli"]
            subtotal = transaction["Subtotal"]
            
            table.add_row([nama_konsumen, nama_barang, no_sku_barang, jumlah_beli, subtotal])

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
    
    def lihat_transaksi_subtotal(self):
        sorted_data = self.insertion_sort(dataTransaksi, key=lambda x: x["Subtotal"])
        table = PrettyTable()
        table.field_names = ["Nama Konsumen", "Nama Barang", "SKU", "Jumlah", "Subtotal (Rp)"]
        for transaksi in sorted_data:
            table.add_row([transaksi["Nama Konsumen"], transaksi["Nama Barang"], transaksi["No. SKU"], transaksi["Jumlah Beli"], transaksi["Subtotal"]])
        print(table)

    # DATA BUATAN
    def insertDummy(self, SKU, nama_barang, harga_satuan, jumlah_stok):
            new_node = Node(SKU, nama_barang, harga_satuan, jumlah_stok)
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


# MENU UTAMA
    def menu_utama(self):
        while True:
            print("\n=== MENU UTAMA ===")
            print("1) Kelola Stok Barang")
            print("2) Kelola Transaksi Konsumen")
            print("0) Exit Program")

            pilih = input("Masukkan pilihan Anda: ")
            if pilih == "1":
                os.system('cls')
                self.kelolaStokBarang()
            elif pilih == "2":
                os.system('cls')
                self.kelolaTransaksiKonsumen()
            elif pilih == "0":
                print('Terimakasih telah menggunakan program kami !')
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                os.system('pause')
                os.system('cls')

# 1. KELOLA STOK BARANG
    def kelolaStokBarang(self):
        while True:
            # SUB MENU (1)
            print("\n=== SUB MENU - KELOLA STOK BARANG ===")
            print("1) Input Data Stok Barang")
            print("2) Restok Barang")
            print("3) Lihat Ketersediaan Barang")
            print("0) Kembali ke MENU UTAMA")

            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                self.input_barang()
                os.system('pause')
                os.system('cls')
            elif pilihan == "2":
                self.restok_barang()
            elif pilihan == "3":
                self.lihat_ketersediaanBarang()
                os.system('pause')
                os.system('cls')
            elif pilihan == "0":
                os.system('cls')
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

# 2. KELOLA TRANSAKSI KONSUMEN
    def kelolaTransaksiKonsumen(self):
        while True:
            # SUB MENU (2)
            print("\n=== SUB MENU - KELOLA TRANSAKSI KONSUMEN ===")
            print("1) Input Data Transaksi Baru")
            print("2) Lihat Data Seluruh Transaksi Konsumen")
            print("3) Lihat Data Transaksi Berdasarkan Subtotal")
            print("0) Kembali ke MENU UTAMA")

            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                self.input_transaksi()
                os.system('pause')
                os.system('cls')
            elif pilihan == "2":
                self.lihat_transaksi_konsumen()
                os.system('pause')
                os.system('cls')
            elif pilihan == "3":
                self.lihat_transaksi_subtotal()
                os.system('pause')
                os.system('cls')
            elif pilihan == "0":
                os.system('cls')
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

# PROGRAM UTAMA
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insertDummy(1111, "Marlboro Merah", 40000, 50)
    bst.insertDummy(2222, "Sampoerna Mild", 30000, 50)
    bst.insertDummy(3333, "Camel Ungu", 25000, 50)
    bst.insertDummy(4444, "Surya Pro 16", 20000, 50)
    bst.menu_utama()