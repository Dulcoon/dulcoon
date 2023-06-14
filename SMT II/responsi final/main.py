class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def print_list(self):
        if self.length == 0:
            print("YOU DON'T HAVE ANY DATA YET!")
        temp = self.head
        while temp is not None:
            print(temp.value, end="")
            if temp.next is not None:
                print(" > ", end="")
            temp = temp.next

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

    def get_values(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(temp.value)
            temp = temp.next
        return values

dll = DoublyLinkedList()
arr = [507, 20, 241, 178, 3, 257, 488, 582, 357, 55, 419, 480, 232, 588, 362, 393, 115, 133, 509,218]    




def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (temp < my_list[j] and j > -1):
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

# pengurtan umur ayam
data = insertion_sort(arr)

# penyeleksian ayam
def seleksi_ayam():
    for i in data:
        if i >= 300:
            dll.append(i)



# output
print("\nList Semua Umur Ayam : ")
print(data)
print("\nList Umur Ayam Yang Akan Diterima (dewasa) : ")
seleksi_ayam()
dll.print_list()    
