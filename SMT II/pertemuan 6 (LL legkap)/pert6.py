# Michael Valensio One Febian
# 5220411200

import os

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList :
    def __init__(self):
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1

        # new_node = Node(value)
        self.head = None
        self.tail = None
        self.length = 0

# dari buku
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
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
        return temp
    
    # daribuku
    def set_value(self, index, value):
        temp = self.get(index)
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


if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.append(2)
    my_linked_list.print_list()

    

    


   
