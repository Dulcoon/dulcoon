import os
import pyinputplus as pyip
from prettytable import PrettyTable
table = PrettyTable()
class barang:
    def __init__(self, SKU, namaBarang, hargaSatuan, jumlahStok):
        self.SKU = SKU
        self.namaBarang = namaBarang
        self.hargaSatuan = hargaSatuan
        self.jumlahStok = jumlahStok
        self.left = None
        self.right = None
class oke:
    def __init__(self):
        pass
    def inputInsert(self):
        namaBarang = input("Masukkan Nama Barang : ")
        hargaSatuan = pyip.inputInt("Masukkan Harga Satuan : ")
        jumlahStok = pyip.inputInt("Masukkan Jumlah Stok Barang : ")
        return namaBarang, hargaSatuan, jumlahStok

    def satunya(self):
        intttt = self.inputInsert()
        aku = barang(intttt)
        print(aku)

# if __name__=="__main":
kelas = oke()
# kelas.inputInsert()
kelas.satunya()
