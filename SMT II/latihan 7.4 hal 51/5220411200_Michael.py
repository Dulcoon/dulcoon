import os
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def printRuteBerangkat(self):
        if self.length == 0:
            print("Belum ada rute ditambahkan")
        temp = self.head
        num = 1
        while temp is not None:
            print(f"{num})",temp.value)
            temp = temp.next
            num += 1

    def printRutePulang(self):
        if self.length == 0:
            print("Belum ada rute ditambahkan")
        temp = self.tail
        num = 1
        while temp is not None:
            print(f"{num})",temp.value)
            temp = temp.prev
            num += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
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
            self.tail.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            print("INDEX INVALID! PLEASE INSERT THE CORRECT INDEX")
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
            print("INDEX INVALID! PLEASE INSERT THE CORRECT INDEX")
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
    
    def appendByIndex(self, value, index):
        new_node = Node(value)
        if index == 0:
            return self.prepend(value)
        temp = self.head
        curIndex = 0
        while temp.next is not None and curIndex < index:
            temp = temp.next
            curIndex += 1
        if temp.next is None and curIndex < index:
            temp.next = new_node
            new_node.prev = temp
            return True
        prev = temp.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = temp
        temp.prev = new_node

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            print("INDEX INVALID! PLEASE INSERT THE CORRECT INDEX")
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
if __name__=="__main__":
    DLL = DoublyLinkedList()
    DLL.append("Jl. Dusun Trini")
    DLL.append("Jl. Siliwangi")
    DLL.append("Jl. Ring Road Utara")
    DLL.append("Jl. Padjajaran")
    DLL.append("Jl. Nyi Tjondrolukito")
    while True:
        print("="*55)
        print("Rute Dari Kost Menuju Tugu Jogja dan Sebaliknya : ")
        print("1. Rute Berangkat")
        print("2. Rute Pulang")
        print("3. Exit")
        print("="*55)
        menu = input("Pilih salah satu dari menu diatas >>")
        if menu == "1":
            print("Rute Berangkat :")
            DLL.printRuteBerangkat()
            input("PRESS [ENTER] To Continue...")
            os.system("cls")
        elif menu == "2":
            print("Rute Pulang :")
            DLL.printRutePulang()
            input("PRESS [ENTER] To Continue...")
            os.system("cls")
        elif menu == "3":
            print("Terimakasih")
            exit()
        else:
            print("Menu Salah")
            continue
