class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def print_rute_berangkat(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def print_rute_pulang(self):
        if self.length == 0:
            return None
        temp = self.tail
        while temp is not None:
            print("-",temp.value)
            temp = temp.prev


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
    
# if __name__=="__main__":
DLL = DoublyLinkedList()
DLL.append("Jl. Kusumanegara")
DLL.append("Jl. Kenari")
DLL.append("Jl. Dr. Sutomo")
DLL.append("Jl. Dr. Wahidin Sudirohusodo")
DLL.append("Jl. Jend. Sudirman")
while True:
    print("Rute Dari Rumah Menuju Tugu Jogja")
    print("1. Jalan Berangkat")
    print("2. Jalan Pulang")
    print("3. Keluar Program")
    menu = input("Masukkan Pilihan Anda : ")
    if menu == "1":
        print("Rute Berangkat :")
        DLL.print_rute_berangkat()
    elif menu == "2":
        print("Rute Pulang")
        DLL.print_rute_pulang()
    elif menu == "3":
        exit()
    else:
        print("Menu Salah")
        continue