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
            print(f"- {temp.value}")
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

    def appendByIndex(self, value, index):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return
        curr = self.head
        curr_index = 0
        while curr.next is not None and curr_index < index:
            curr = curr.next
            curr_index += 1
        if curr.next is None and curr_index < index:
            curr.next = new_node
            new_node.prev = curr
            return
        prev = curr.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = curr
        curr.prev = new_node

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

    def getToChange(self, index):
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
        return temp 

    def deleteByIndex(self, index):
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        temp = self.head
        temp_index = 0
        while temp is not None and temp_index != index:
            temp = temp.next
            temp_index += 1
        if temp is not None:
            temp.prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev
        else:
            print("INDEX NOT FOUND")
        

    def set_value(self, index, value):
        temp = self.getToChange(index)
        if temp:
            temp.value = value
            return True
        return False


        
if __name__=="__main__":
    my_doubly_linked_list = DoublyLinkedList()


    while True:
        print("MENU")
        print("1. ADD LIST")
        print("2. ADD LIST BY INDEX")
        print("3. UPDATE LIST BY INDEX")
        print("4. DELETE FIRST LIST")
        print("5. DELETE LIST BY INDEX")
        print("6. SEARCH LIST BY INDEX")
        print("7. LIST TO DO")
        print("8. EXIT")
        menu = input("INSERT YOUR CHOICE HERE >> : ")
        if menu == '1':
            appe = input("INSERT YOUR DATA : ")
            my_doubly_linked_list.append(appe)
            print("DATA SUCCESSFULLY ADDED!")
            os.system("pause")
            os.system("cls")
        elif menu == '2':
            idx = int(input("PLEASE INPUT THE INDEX WHERE YOU WANT TO ADD YOUR DATA : "))
            val = input("PLEASE INPUT YOUR DATA : ")
            my_doubly_linked_list.appendByIndex(val, idx)
            print(f"YOUR DATA SUCCESSFULLY ADDED IN INDEX NUMBER {idx} ")
            os.system("pause")
            os.system("cls")
        elif menu == '3':
            idx = int(input("PLEASE INPUT THE INDEX WHERE YOU WANT TO UPDATE YOUR DATA : "))
            print(f"YOUR CURRENT DATA IN INDEX NUMBER {idx} IS : \n{my_doubly_linked_list.get(idx)}")
            val = input("PLEASE INPUT YOUR NEW DATA : ")
            my_doubly_linked_list.set_value(idx, val)
            print(f"YOUR DATA SUCCESSFULLY UPDATED ")
            os.system("pause")
            os.system("cls")
        elif menu == '4':
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
        elif menu == '5':
            idx = int(input("INSERT THE DATA'S INDEX THAT YOU WANT TO DELETE :  "))
            print(f"DATA IN INDEX NUMBER {idx} IS : \n{my_doubly_linked_list.get(idx)}")
            y = input(f"ARE YOU SURE WANT TO DALETE THE DATA? <y/n> ")
            if y.lower() == "y":
                my_doubly_linked_list.deleteByIndex(idx)
                print(f"DATA NUMBER {idx} IS SUCCESFULLY DELETED")
                os.system("pause")
                os.system("cls")
            else:
                print("DELETE DATA CALCELED")
                os.system("pause")
                os.system("cls")
        elif menu == '6':
            idxx = int(input("INSERT THE DATA'S INDEX THAT YOU WANT TO SEARCH :  "))
            print(f"DATA IN INDEX NUMBER {idxx} IS : \n{my_doubly_linked_list.get(idxx)}")
            os.system("pause")
            os.system("cls")
        elif menu == '7':
            print("TO DO LIST : ")
            my_doubly_linked_list.print_list()
            os.system("pause")
            os.system("cls")
        elif menu == '8':
            print("THANKS FOR USING MY PROGRAM")
            exit()
        else:
            print("WE DON'T UNDERSTAND, PLEASE INSERT THE CORRECT MENU!")
            input("[PRESS ANYTHING TO RE-INPUT MENU]")
            os.system("cls")