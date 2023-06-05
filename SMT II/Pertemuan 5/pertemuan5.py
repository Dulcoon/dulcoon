# # Michael Valensio One Febian
# # 5220411200

# import os

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList :
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
    
# """
# ini print dengan index
# """
        
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
#     #             i += 1 # meningkatkan nomor urut setiap iterasi


#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
        
#     def addContact(self, Nama, NoHp):
#         kontakString = f"{Nama} {NoHp}"
#         self.append(kontakString)

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#             self.head = None
#         return temp

#     def find_by_name(self, name):
#         temp = self.head
#         while temp is not None:
#             if name in temp.value:
#                 return temp.value.split()[1]  # mengembalikan nomor HP
#             temp = temp.next
#         # print("kontak tidak ada")
#         return ("Kontak tidak ada")

#     def remove_by_name(self, name):
#         if self.length == 0:
#             print("Kontak kosong")
#             return False

#         temp = self.head
#         pre = None
#         while temp is not None:
#             if temp.value[0].lower() == name.lower():
#                 print(temp.value)
#                 val = input("Are u sure? <y/n>")
#                 if val.lower() == 'y':
#                     # hapus elemen
#                     if pre is None:
#                         self.head = temp.next
#                     elif temp.next is None:
#                         self.tail = pre
#                         self.tail.next = None
#                     else:
#                         pre.next = temp.next
#                     self.length -= 1
#                     print(f"Contact {name} has successfully deleted.")
#                     return True
#                 pre = temp
#                 temp = temp.next
                    
#         # jika nama tidak ditemukan
#         print("Nama kontak tidak ditemukan")
#         return False

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
    
#     # dari buku
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp
#     # dari buku
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
#     # daribuku
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     # dari buku
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         temp = self.get(index - 1)
#         new_node.next = temp.next
#         temp.next = new_node
#         self.length+=1
#         return True

#     def clear(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def remove_at(self, index):
#         if index < 0 or index >= self.length:
#             print("Index diluar rentang yang valid.")
#             return None
#         elif index == 0:
#             removed_node = self.head
#             self.head = removed_node.next
#             removed_node.next = None
#             self.length -= 1
#             if self.length == 0:
#                 self.tail = None
#             return removed_node
#         else:
#             pre = self.head
#             cur = pre.next
#             i = 1
#             while cur is not None:
#                 if i == index:
#                     removed_node = cur
#                     pre.next = cur.next
#                     removed_node.next = None
#                     self.length -= 1
#                     if index == self.length:
#                         self.tail = pre
#                     return removed_node
#                 pre = cur
#                 cur = cur.next
#                 i += 1
            
#         #dari buku 


# if __name__ == "__main__":
#     my_linked_list = LinkedList(5)
#     my_linked_list.append(4)
#     my_linked_list.append(3)
#     my_linked_list.append(2)
#     my_linked_list.append(1)
#     my_linked_list.print_list()

