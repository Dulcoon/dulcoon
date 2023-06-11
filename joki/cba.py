import os

def inputInt(text):
    while True:
        try:
            var = int(input(text))
            return var
        except:
            print("Hanya Masukkan Angka!")

class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def _init_(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value["nomor"] == temp.value["nomor"]:
                return False
            if new_node.value["nomor"] < temp.value["nomor"]:
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
            if value < temp.value["nomor"]:
                temp = temp.left
            elif value > temp.value["nomor"]:
                temp = temp.right
            else:
                return True
        return False
    
    def get(self, value):
        temp = self.root
        while temp:
            if value < temp.value['nomor']:
                temp = temp.left
            elif value > temp.value['nomor']:
                temp = temp.right
            else:
                return temp.value
        return False
    

def main():
    sitorsi = BinarySearchTree()
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
                    print("0. Kembali\n")
                    inputMenuBarang= inputInt("Pilih menu [0-2] : ")
                    if inputMenuBarang == 1:
                        print("============= Input Data Stok Barang ==============")
                        nomor = inputInt("Masukkan No. SKU (4 digit) : ")
                        while len(str(nomor)) > 4:
                            nomor = inputInt("Masukkan No. SKU (4 digit) : ")
                        if sitorsi.contains(nomor):
                            print("Maaf No. SKU Sudah Ada!")
                            continue
                        nama = input("Masukkan Nama Barang: ")
                        harga = inputInt("Masukkan Harga Barang: ")
                        jumlah = inputInt("Masukkan Jumlah Stok Barang: ")
                        data = [nomor, nama, harga, jumlah]
                        if sitorsi.insert(data):
                            print("Barang Berhasil ditambahkan")
                        else:
                            print("Barang Gagal ditambahkan")