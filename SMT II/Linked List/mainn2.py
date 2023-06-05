class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next


linked_list = LinkedList()

while True:
    print("\nMenu")
    print("1. Append")
    print("2. Remove")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter data to append: ")
        linked_list.append(data)

    elif choice == "2":
        data = input("Enter data to remove: ")
        linked_list.remove(data)

    elif choice == "3":
        linked_list.display()

    elif choice == "4":
        break

    else:
        print("Invalid choice. Try again.")
