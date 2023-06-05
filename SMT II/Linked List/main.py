import os

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList :
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

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
        
    # def print_list(self):
    #     if self.length == 0:
    #         print("kontak kosong")
    #     else:
    #         temp = self.head 
    #         i = 1
    #         while temp is not None:
    #             if i > 0:
    #                 contact_string = f"{i}. {temp.value}"
    #                 print(contact_string)
    #             temp = temp.next
    #             i += 1 # meningkatkan nomor urut setiap iterasi

    # def print_list(self):
    #     if self.length == 1:
    #         print("kontak kosong")
    #     else:
    #         temp = self.head 
    #         i = 0
    #         while temp is not None:
    #             if i > 0:
    #                 contact_string = f"{i}. {temp.value}"
    #                 print(contact_string)
    #             temp = temp.next
    #             i += 1 # meningkatkan nomor urut setiap iterasi
    

    def addContact(self, Nama, NoHp):
        kontakString = f"{Nama} {NoHp}"
        self.append(kontakString)

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

    def find_by_name(self, name):
        temp = self.head
        while temp is not None:
            if name in temp.value:
                return temp.value.split()[1]  # mengembalikan nomor HP
            temp = temp.next
        # print("kontak tidak ada")
        return ("Kontak tidak ada")

    def remove_by_name(self, name):
        if self.length == 0:
            print("Kontak kosong")
            return False

        temp = self.head
        pre = None
        while temp is not None:
            if temp.value[0].lower() == name.lower():
                print(temp.value)
                val = input("Are u sure? <y/n>")
                if val.lower() == 'y':
                    # hapus elemen
                    if pre is None:
                        self.head = temp.next
                    elif temp.next is None:
                        self.tail = pre
                        self.tail.next = None
                    else:
                        pre.next = temp.next
                    self.length -= 1
                    print(f"Contact {name} has successfully deleted.")
                    return True
                pre = temp
                temp = temp.next
                    
        # jika nama tidak ditemukan
        print("Nama kontak tidak ditemukan")
        return False



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



my_linked_list = LinkedList("Sampel")

while True:
    print("Menu Linked List")
    print("1. Show All Contact\n2. Add New Contact\n3. Search Contact\n4. Delete Contact")
    menu = int(input("Masukkan Menu Yang Anda Inginkan : "))
    if menu > 5:
        print("Menu Salah")
    elif menu == 1:
        my_linked_list.print_list()
        input("TEKAN APAPUN UNTUK MELANJUTKAN")
        os.system("cls")
    elif menu == 2:
        nama = input("Please Input Contact Name : ")
        noHp = input("Input Phone Number : ")
        my_linked_list.addContact(nama, noHp)
        os.system('cls')
    elif menu == 3:
        nama = input("Input Contact Name : ")
        no = my_linked_list.find_by_name(nama)
        print(no)
    elif menu == 4:
        print("Delete Data Menu : ")
        pil = input("a) Delete All Contact\nb) Delete By Index\nc)Delete by Name\n>>")
        if pil.lower() == 'a':
            a = input("Are You Sure Delete All data? <y/n >")
            if a.lower() == 'y':
                my_linked_list.clear()
            else:
                continue
        elif pil.lower() == 'b':
            my_linked_list.print_list()
            index = int(input("Input data index to delete : "))
            a = input(f"Are You Sure Delete data in index {index}? <y/n >")
            if a.lower() == 'y':
                my_linked_list.remove_at(index)
                print(f"Data with index {index} has successfully deleted.")
            else:
                continue
        elif pil.lower() == 'c':
            my_linked_list.print_list()
            contactName = input("Input contact name : ")
            my_linked_list.remove_by_name(contactName)
            
    elif menu == 5:
        nm = input("Please Input Contact Name : ")
        my_linked_list.remove_by_name(nm)
    elif menu == 6:
        # nm = input("Please Input Contact Name : ")
        my_linked_list.pop()
        


    


