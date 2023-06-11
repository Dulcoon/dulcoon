import os

def inputInt(text):
    while True:
        try:
            var = int(input(text))
            return var
        except:
            print("Hanya Masukkan Angka!")

class Node:
    def __init__(self, nosku, nama_barang, harga_satuan, jumlah_stok):
        self.nosku = nosku
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, nosku, nama_barang, harga_satuan, jumlah_stok):
        new_node = Node(nosku, nama_barang, harga_satuan, jumlah_stok)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.nosku == temp.nosku:
                return False
            if new_node.nosku < temp.nosku:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.nosku:
                temp = temp.left
            elif value > temp.nosku:
                temp = temp.right
            else:
                return True
        return False
    
    def get(self, value):
        temp = self.root
        while temp:
            if value < temp.nosku:
                temp = temp.left
            elif value > temp.nosku:
                temp = temp.right
            else:
                return temp.value
        return False
    
    def print_stok_barang(self):
        stack = []
        temp = self.root

        while True:
            if temp is not None:
                stack.append(temp)
                temp = temp.left
            elif stack:
                temp = stack.pop()
                print("No. SKU:", temp.nosku)
                print("Nama Barang:", temp.nama_barang)
                print("Harga Satuan:", temp.harga_satuan)
                print("Jumlah Stok:", temp.jumlah_stok)
                print("--------------------")
                temp = temp.right
            else:
                break
    

def main():
    sitorsi = BinarySearchTree()
    sitorsi.insert(3333, "baju", 20000, 33)
    sitorsi.insert(4444, "celana", 20000, 31)
    sitorsi.insert(5555, "sepatu", 20000, 34)
    while True:
            os.system ('cls')
            print("\n======================================")
            print("============ Menu Utama ==============")
            print("======================================")
            print("1. Kelola Stok Barang")
            print("2. Kelola Transaksi Konsumen")
            print("0. Keluar\n")
            inputMenu= inputInt("Pilih menu [0-2] : ")
            if inputMenu == 1:
                while True:
                    os.system ('cls')
                    print("\n========================================")
                    print("============ Menu Kelola Stok Barang ==========")
                    print("========================================")
                    print("1. Input Data Stok Barang")
                    print("2. Restok Barang")
                    print("3. Lihat Stok Barang")
                    print("0. Kembali\n")
                    inputMenuBarang= inputInt("Pilih menu [0-2] : ")
                    if inputMenuBarang == 1:
                        print("============= Input Data Stok Barang ==============")
                        nomor = inputInt("Masukkan No. SKU (4 digit) : ")
                        while len(str(nomor)) > 4:
                            nomor = inputInt("Masukkan No. SKU (4 digit) : ")
                        if sitorsi.contains(nomor):
                            print("Maaf No. SKU Sudah Ada!")
                            os.system ('pause')
                            continue
                        nama = input("Masukkan Nama Barang: ")
                        harga = inputInt("Masukkan Harga Barang: ")
                        jumlah = inputInt("Masukkan Jumlah Stok Barang: ")
                        if sitorsi.insert(nomor, nama, harga, jumlah):
                            print("Barang Berhasil ditambahkan")
                        else:
                            print("Barang Gagal ditambahkan")
                    elif inputMenuBarang == 3:
                        sitorsi.print_stok_barang()
                    elif inputMenuBarang == 0:
                        main()
                    os.system ('pause')
if __name__ == "__main__":
    main()