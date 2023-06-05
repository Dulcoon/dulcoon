import os
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def print_Queue(self):
        if self.length == 0:
            return None
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length==0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value
    
    def max(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            print("You only have 1 data")
        li = []
        temp = self.first
        while temp is not None:
            li.append(temp.value)
            temp = temp.next
        max_value = max(li)
        return max_value
    
    def min(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            print("You only have 1 data")
        li = []
        temp = self.first
        while temp is not None:
            li.append(temp.value)
            temp = temp.next
        min_value = min(li)
        return min_value
    
    def peek_first(self):
        return self.first.value
    
    def peek_last(self):
        return self.last.value
    
    def length_check(self):
        return self.length
    
    def desperation(self, x):
        if x < 1 or x > self.length:
            return None

        temp = self.first
        for _ in range(self.length - x - 1):  # Mengubah batas perulangan
            temp = temp.next

        pre = temp
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp



if __name__=="__main__":
    my_Queue = Queue()
    while True:
        print("="*20)
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Print")
        print("4. Max Value")
        print("5. Min Value")
        print("6. Peek first")
        print("7. Peek last")
        print("8. length Check")
        print("="*20)
        menu = input("Masukkan Menu Yang Diinginkan : ")
        if menu == "1":
            val = int(input("Masukkan data baru : "))
            my_Queue.enqueue(val)
            print("Enqueue Successfull")
            os.system("pause")
            os.system("cls")
        elif menu == "2":
            print(my_Queue.dequeue(), "Has been removed from Queue")
            os.system("pause")
            os.system("cls")
        elif menu == "3":
            my_Queue.print_Queue()
            os.system("pause")
            os.system("cls")
        elif menu == "4":
            print("Max Value is", my_Queue.max())
            os.system("pause")
            os.system("cls")
        elif menu == "5":
            print("Min Value is", my_Queue.min())
            os.system("pause")
            os.system("cls")
        elif menu == "6":
            print("first Value is", my_Queue.peek_first())
            os.system("pause")
            os.system("cls")
        elif menu == "7":
            print("last Value is", my_Queue.peek_last())
            os.system("pause")
            os.system("cls")
        elif menu == "8":
            print("Queue's length is : ", my_Queue.length_check())
            os.system("pause")
            os.system("cls")
        elif menu == "9":
            # print("Queue's length is : ", my_Queue.length_check())
            x = int(input("Masukkan X : "))
            print(my_Queue.desperation(x))
            os.system("pause")
            os.system("cls")



            


# my_Queue.push(6)
# my_Queue.push(7)
# # my_Queue.print_Queue()
# my_Queue.print_Queue()