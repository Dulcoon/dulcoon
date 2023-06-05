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

    def print_list(self):
        if self.length == 0:
            print("YOU DON'T HAVE ANY DATA YET!")
        temp = self.head
        while temp is not None:
            print(temp.value)
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
        # return temp 
        if temp:
            temp.value = value
            return True
        return False

# =========================================================================

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

    # def appendByIndex(self, value, index):
    #     new_node = Node(value)
    #     if index == 0:
    #         return self.prepend(value)
        

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
    my_doubly_linked_list = DoublyLinkedList()

    while True:
        print("MENU")
        print("1. ADD LIST")
        print("2. ADD FIRST LIST")
        print("3. ADD LIST BY INDEX")
        print("4. UPDATE LIST BY INDEX")
        print("5. DELETE FIRST LIST")
        print("6. DELETE LIST BY INDEX")
        print("7. SEARCH LIST BY INDEX")
        print("8. LIST TO DO")
        print("9. EXIT")
        menu = input("INSERT YOUR CHOICE HERE >> : ")
        if menu == '1':
            appe = input("INSERT YOUR DATA : ")
            my_doubly_linked_list.append(appe)
            print("DATA SUCCESSFULLY ADDED!")
            os.system("pause")
            os.system("cls")
        elif menu == '2':
            appe = input("INSERT YOUR DATA : ")
            my_doubly_linked_list.prepend(appe)
            print("DATA SUCCESSFULLY ADDED!")
            os.system("pause")
            os.system("cls")
        elif menu == '3':
            idx = int(input("PLEASE INPUT THE INDEX WHERE YOU WANT TO ADD YOUR DATA : "))
            val = input("PLEASE INPUT YOUR DATA : ")
            my_doubly_linked_list.appendByIndex(val, idx)
            print(f"YOUR DATA SUCCESSFULLY ADDED IN INDEX NUMBER {idx} ")
            os.system("pause")
            os.system("cls")
        elif menu == '4':
            idx = int(input("PLEASE INPUT THE INDEX WHERE YOU WANT TO UPDATE YOUR DATA : "))
            print(f"YOUR CURRENT DATA IN INDEX NUMBER {idx} IS : \n{my_doubly_linked_list.get(idx)}")
            val = input("PLEASE INPUT YOUR NEW DATA : ")
            my_doubly_linked_list.set_value(idx, val)
            print(f"YOUR DATA SUCCESSFULLY UPDATED ")
            os.system("pause")
            os.system("cls")
        elif menu == '5':
            y = input("ARE YOU SURE WANT TO DALETE THE FIRST DATA? <y/n> ")
            if y.lower() == "y":
                my_doubly_linked_list.pop_first()
                print("YOUR FIRST DATA IS SUCCESFULLY DELETED")
                os.system("pause")
                os.system("cls")
            else:
                print("DELETE DATA CALCELED")
                os.system("pause")
                os.system("cls")
        elif menu == '6':
            idx = int(input("INSERT THE DATA'S INDEX THAT YOU WANT TO DELETE :  "))
            print(f"DATA IN INDEX NUMBER {idx} IS : \n{my_doubly_linked_list.get(idx)}")
            y = input(f"ARE YOU SURE WANT TO DALETE THE DATA? <y/n> ")
            if y.lower() == "y":
                my_doubly_linked_list.remove_at_index(idx)
                print(f"DATA NUMBER {idx} IS SUCCESFULLY DELETED")
                os.system("pause")
                os.system("cls")
            else:
                print("DELETE DATA CALCELED")
                os.system("pause")
                os.system("cls")
        elif menu == '7':
            idxx = int(input("INSERT THE DATA'S INDEX THAT YOU WANT TO SEARCH :  "))
            print(f"DATA IN INDEX NUMBER {idxx} IS : \n{my_doubly_linked_list.get(idxx)}")
            os.system("pause")
            os.system("cls")
        elif menu == '8':
            print("TO DO LIST : ")
            my_doubly_linked_list.print_list()
            os.system("pause")
            os.system("cls")
        elif menu == '9':
            print("THANKS FOR USING MY PROGRAM")
            exit()
        else:
            print("WE DON'T UNDERSTAND, PLEASE INSERT THE CORRECT MENU!")
        #     input("[PRESS ANYTHING TO RE-INPUT MENU]")
            os.system("pause")
            os.system("cls")