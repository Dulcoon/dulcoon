# Michael Valensio One Febian
# 5220411200

import os
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# dari buku
    def print_list(self):
        if self.length == 0:
            print("data empty")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def print_list_LinkedList(self):
        if self.length == 0:
            print("data empty")
        temp = self.head
        while temp is not None:
            print(temp.value, end="")
            if temp.next is not None:
                print(" -> ", end="")
            temp = temp.next


# dari buku
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

# dari buku
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp



# dari buku
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
# dari buku
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    # dari buku
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    # daribuku
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        if temp:
            temp.value = value
            return True
        return False
    
# dari buku
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

# dari buku
    def remove(self, index):
        if index < 0 or index > self.length :
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            print("Index diluar rentang yang valid.")
            return None
        elif index == 0:
            removed_node = self.head
            self.head = removed_node.next
            removed_node.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return removed_node
        else:
            pre = self.head
            cur = pre.next
            i = 1
            while cur is not None:
                if i == index:
                    removed_node = cur
                    pre.next = cur.next
                    removed_node.next = None
                    self.length -= 1
                    if index == self.length:
                        self.tail = pre
                    return removed_node
                pre = cur
                cur = cur.next
                i += 1
            
    def sort(self):
        if self.length <= 1:
         return None
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.value)
            temp = temp.next
        arr.sort()
        temp = self.head
        for i in range(len(arr)):
            temp.value = arr[i]
            temp = temp.next
            
    def sortDCD(self):
        if self.length <= 1:
         return None
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.value)
            temp = temp.next
        arr.sort(reverse=True)
        temp = self.head
        for i in range(len(arr)):
            temp.value = arr[i]
            temp = temp.next
        #dari buku 

    def load(self):
        bar = [
            " K       ",
            " KO      ",
            " KON     ",
            " KONT    ",
            " KONTO   ",
            " KONTOL  ",
            " KONTOLL ",
            " KONTOLLL",
        ]
        i = 0

        while True:
            print("MUKA KAMU KAYAK"+bar[i % len(bar)], end="\r")
            time.sleep(.2)
            i += 1
            if i == 17:
                break

    def reverse_list(self):
        # jika list kosong atau hanya memiliki satu elemen
        if self.head is None or self.head.next is None:
            return

        # menginisialisasi node terakhir sebagai node pertama
        prev = None
        temp = self.head

        # melakukan reverse pada setiap node
        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        # mengupdate head dan tail
        self.tail = self.head
        self.head = prev


if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.append(2)
    my_linked_list.append(4)
    my_linked_list.append(6)
    my_linked_list.append(8)
    my_linked_list.append(10)
    my_linked_list.append(3)
    my_linked_list.append(5)
    my_linked_list.append(7)
    my_linked_list.append(9)
    my_linked_list.append(1)
    while True:
        print("Program Linked List")
        print("1. Append")
        print("2. Pop")
        print("3. Prepend")
        print("4. Pop First")
        print("5. Get")
        print("6. Set")
        print("7. insert")
        print("8. Remove")
        print("9. Urutkan Data")
        print("10. Print List")
        print("11. Print List (Format Linked List)")
        print("12. Clear")
        print("13. Reverse List")
        print("14. Exit")
        menu = input("Masukkan kontol mu disini : ")
        if menu == "1":
            while True:
                try:
                    val = int(input("Masukkan kontol kamu di laptop ini : "))
                except ValueError:
                    print("Input Harus Berupa Integer (Ngewe) ")
                else:
                    my_linked_list.load()
                    my_linked_list.append(val)
                    print("Data Telah Berhasil Di entot!")
                    input("PRESS [MEMEK] TO CONTINUE ")
                    os.system("cls")
                    break
        elif menu == "2":
            yk = input("Apakah anda yakin ingin mengentot yang terakhir? <y/n> ")
            if yk.lower() == "y":
                my_linked_list.load()
                my_linked_list.pop()
                print("Data Berhasil Dientot!")
            else:
                print("Operasi telah dikulum.")
            input("PRESS [MEMEK] TO CONTINUE ")
            os.system("cls")
        elif menu == "3":
            while True:
                try:
                    val = input("Masukkan Data Yang Ingin di ewe : ")
                except ValueError:
                    print("Input Harus Berupa Integer (Ngentot) ")
                else:
                    my_linked_list.load()
                    my_linked_list.prepend(val)
                    print("Data Telah Berhasil Di entot paksa!")
                    input("PRESS [MEMEK] TO CONTINUE ")
                    os.system("cls")
                    break
        elif menu == "4":
            yk = input("Apakah anda yakin ingin menghapus data Pertama? <y/n> ")
            if yk.lower() == "y":
                my_linked_list.load()
                my_linked_list.pop_first()
                print("Data Berhasil Dihapus!")
            else:
                print("Operasi telah dibatalkan.")
            input("PRESS [ENTER] TO CONTINUE ")
            os.system("cls")
        elif menu == "5":
            while True:
                try:
                    idx = int(input("Masukkan Index : "))
                except ValueError:
                    print("Index Harus Berupa Integer (Numerik) ")
                else:
                    my_linked_list.load()
                    print(f"Data Di Index Ke {idx} Adalah {my_linked_list.get(idx)}")
                    input("PRESS [ENTER] TO CONTINUE ")
                    os.system("cls")
                    break
        elif menu == "6":
            while True:
                try:      
                    idx = int(input("Masukkan Index : "))
                except ValueError:
                    print("Index Harus Berupa Integer (Numerik) ")
                else:
                    print(f"Data Di Index Ke {idx} Adalah {my_linked_list.get(idx)}")
                    yk = input("Apakah anda yakin ingin merubah data tersebut? <y/n> ")
                    if yk.lower() == "y":
                        while True:
                            try:
                                val = int(input("Masukkan Data Yang Baru : "))
                            except ValueError:
                                print("Input Harus Berupa Integer (Numerik) ")
                            else:
                                my_linked_list.load()
                                my_linked_list.set_value(idx,val)
                                print("Data Telah Berhasil Diubah!")
                                my_linked_list.print_list_LinkedList()
                                input("PRESS [ENTER] TO CONTINUE ")
                                os.system("cls")
                                break
                    else:
                        print("Operasi telah dibatalkan.")
                        input("PRESS [ENTER] TO CONTINUE ")
                        os.system("cls")
                    break
        elif menu == "7":
            idx = int(input("Masukkan Index : "))
            val = input("Masukkan Data Yang Ingin Ditambahkan : ")
            my_linked_list.load()
            my_linked_list.insert(idx,val)
            print("Data Telah Berhasil Ditambahkan!")
            input("PRESS [ENTER] TO CONTINUE ")
            os.system("cls")
        elif menu == "8":
            idx = int(input("Masukkan Index : "))
            yk = input(f"Data di index ke {idx} adalah {my_linked_list.get(idx)} \nApakah anda yakin ingin menghapus data tersebut? <y/n> ")
            if yk.lower() == "y":
                my_linked_list.load()
                my_linked_list.remove_at(idx)
                print("Data Telah Berhasil Dihapus!")
                liat = input("Apakah anda ingin langsung melihat data terbaru? <y/n> ")
                if liat.lower() == "y":
                        my_linked_list.print_list_LinkedList()
                        input("PRESS [ENTER] TO CONTINUE ")
                        os.system("cls")
                else:
                    os.system("cls")
                    continue
            else:
                print("Operasi telah dibatalkan.")
                input("PRESS [ENTER] TO CONTINUE ")
                os.system("cls")
        elif menu == "9":
            while True:
                ask = input("1. Ascending\n2. Descending\n>> ")
                if ask == "1":
                    my_linked_list.load()
                    my_linked_list.sort()
                    print("Data Telah Berhasil Diurutkan!")
                    my_linked_list.print_list_LinkedList()
                    input("\nPRESS [ENTER] TO CONTINUE ")
                    os.system("cls")
                    break
                elif ask == "2":
                    my_linked_list.load()
                    my_linked_list.sortDCD()
                    print("Data Telah Berhasil Diurutkan!")
                    my_linked_list.print_list_LinkedList()
                    input("\nPRESS [ENTER] TO CONTINUE ")
                    os.system("cls")
                    break
                else:
                    print("Input salah!")
        elif menu == "10":
            my_linked_list.print_list()
            input("PRESS [ENTER] TO CONTINUE ")
            os.system("cls")
        elif menu == "11":
            my_linked_list.print_list_LinkedList()
            input("\nPRESS [ENTER] TO CONTINUE ")
            os.system("cls")
        elif menu == "12":
            ask = input("Dengan Memilih Menu Ini Maka Semua Data Anda Akan Hilang.\nApakah Anda Yakin? <y/n>")
            if ask.lower() == "y":
                my_linked_list.load()
                my_linked_list.clear()
                os.system("cls")
                print("Semua Data Telah Dihapus!")
                input("PRESS [ENTER] TO CONTINUE ")
                os.system("cls")
            else:
                print("Operasi Dibatalkan.")
                input("PRESS [ENTER] TO CONTINUE ")
                os.system("cls")
        elif menu == "13":
                my_linked_list.load()
                my_linked_list.reverse_list()
                print("List Telah Berhasil Di Reverse")
                input("PRESS [ENTER] TO CONTINUE ")
                os.system("cls")
        elif menu == "14":
            exit()
        else:
            print("Menu Yang Anda Masukkan Tidak Valid!")
            input("PRESS [ENTER] TO CONTINUE ")
            os.system("cls")
            


            




    

    


   
