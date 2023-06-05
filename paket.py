import os
from prettytable import PrettyTable


class Node:
    def __init__(self, noResi, namaPenerima, alamatPenerima, noTeleponPenerima, beratPaket, jenisPaket, sttsPengiriman):
        self.noResi = noResi
        self.naPen = namaPenerima
        self.alPen = alamatPenerima
        self.noTelepon = noTeleponPenerima
        self.beratPaket = beratPaket
        self.jenis = jenisPaket
        self.stts = sttsPengiriman
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        myTable = PrettyTable(["No Resi", "Nama Penerima", "Alamat Penerima", "No Tlp Penerima", "Berat Paket (Kg)", "Jenis Paket", "Status Pengiriman"])
        temp = self.head
        while temp is not None:
            myTable.add_row([temp.noResi, temp.naPen, temp.alPen, temp.noTelepon, temp.beratPaket, temp.jenis, temp.stts])
            temp = temp.next
        print(myTable)
    # def print_list(self):
    #     print(myTable)

    def append(self, noResi, namaPenerima, alamatPenerima, noTeleponPenerima, beratPaket, jenisPaket, sttsPengiriman):
        new_node = Node(noResi, namaPenerima, alamatPenerima, noTeleponPenerima, beratPaket, jenisPaket, sttsPengiriman)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # myTable.add_row(value)  
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            # myTable.add_row(value)  
        self.length += 1
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp.value

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        if temp:
            temp.value = value
            return True
        return False

    def ubah_status(self, resi, status):
        if self.length == 0:
            print("Data Kosong")
        temp = self.head
        while temp is not None:
            if temp.noResi == resi:
                temp.stts = status
            temp.next
        print("No Resi Tidak Ditemukan")
            

    def remove(self,index):
        if index < 0 or index > 0 >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1 )
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        if self.length == 0 or self.length == 1:
            return
        current_node = self.head
        while current_node is not None:
            temp = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp
            current_node = temp
        temp = self.head
        self.head = self.tail
        self.tail = temp

class Package:
    def __init__(self, noResi, namaPenerima, alamatPenerima, noTeleponPenerima, beratPaket, jenisPaket, sttsPengiriman):
        self.noResi = noResi
        self.naPen = namaPenerima
        self.alPen = alamatPenerima
        self.noTelepon = noTeleponPenerima
        self.beratPaket = beratPaket
        self.jenis = jenisPaket
        self.stts = sttsPengiriman

my_doubly_linked_list = DoublyLinkedList()

while True:
    print("MENU")
    print("1. Tambahkan Paket")
    print("2. Ubah Status Paket")
    print("3. Hapus Paket (Sudah Diterima)")
    print("4. Cari Paket")
    print("5. Tampilkan Semua data paket")
    menu = input("Masukkan menu yang diinginkan : ")
    if menu == "1":
        noResi = input("Masukkan No resi : ")
        namaPenerima = input("Masukkan Nama Penerima : ")
        alamatPenerima = input("Masukkan Alamat Penerima : ")
        noTeleponPenerima = input("Masukkan No Tlp Penerima : ")
        beratPaket = int(input("Masukkan Berat Paket (Kg) : "))
        jenisPaket = input("Masukkan Jenis Paket : ")
        sttsPengiriman = input("Masukkan Status Pengiriman Paket : ")
        # paket = Package(noResi, namaPenerima, alamatPenerima, noTeleponPenerima, beratPaket, jenisPaket, sttsPengiriman)
        my_doubly_linked_list.append(noResi, namaPenerima, alamatPenerima, noTeleponPenerima, beratPaket, jenisPaket, sttsPengiriman)
        print("Data Berhasil Ditambahkan")
        os.system("pause")
        os.system("cls")
    elif menu == "2":
        resi = int(input("Masukan Nomor Resi (Numerik Only) : "))
        stat = int(input("Masukkan status paket <1. Dalam Perjalanan>"))
        if stat == 1:
            statu = "Sedang Dalam Perjalanan"
        if stat == 2:
            statu = "Sudah Diterima"
        my_doubly_linked_list.ubah_status(resi, statu)
    if menu == "5":
        my_doubly_linked_list.print_list()
    
