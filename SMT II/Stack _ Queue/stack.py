import os
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        # new_node = Node(value)
        self.top = None
        self.bottom = None
        self.height = 0

    def print_stack(self):
        if self.height == 0:
            return None
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height==0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height==0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value
    
    def max(self):
        if self.height == 0:
            return None
        elif self.height == 1:
            print("You only have 1 data")
        li = []
        temp = self.top
        while temp is not None:
            li.append(temp.value)
            temp = temp.next
        max_value = max(li)
        return max_value
    
    def min(self):
        if self.height == 0:
            return None
        elif self.height == 1:
            print("You only have 1 data")
        li = []
        temp = self.top
        while temp is not None:
            li.append(temp.value)
            temp = temp.next
        min_value = min(li)
        return min_value
    
    def peek_top(self):
        return self.top.value
    
    def peek_bottom(self):
        return self.bottom.value
    
    def height_check(self):
        return self.height
    

if __name__=="__main__":
    my_stack = Stack()
    while True:
        print("="*20)
        print("1. Push")
        print("2. Pop")
        print("3. Print")
        print("4. Max Value")
        print("5. Min Value")
        print("6. Peek top")
        print("7. Peek bottom")
        print("8. Height Check")
        print("="*20)
        menu = input("Masukkan Menu Yang Diinginkan : ")
        if menu == "1":
            val = int(input("Masukkan data baru : "))
            my_stack.push(val)
            print("Push Successfull")
            os.system("pause")
            os.system("cls")
        elif menu == "2":
            print(my_stack.pop(), "Has been removed from stack")
            os.system("pause")
            os.system("cls")
        elif menu == "3":
            my_stack.print_stack()
            os.system("pause")
            os.system("cls")
        elif menu == "4":
            print("Max Value is", my_stack.max())
            os.system("pause")
            os.system("cls")
        elif menu == "5":
            print("Min Value is", my_stack.min())
            os.system("pause")
            os.system("cls")
        elif menu == "6":
            print("Top Value is", my_stack.peek_top())
            os.system("pause")
            os.system("cls")
        elif menu == "7":
            print("Bottom Value is", my_stack.peek_bottom())
            os.system("pause")
            os.system("cls")
        elif menu == "8":
            print("Stack's Height is : ", my_stack.height_check())
            os.system("pause")
            os.system("cls")



# my_stack.push(6)
# my_stack.push(7)
# # my_stack.print_stack()
# my_stack.print_stack()