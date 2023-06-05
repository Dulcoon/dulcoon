class Node:
    # parameter nama dan score
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_score(self, name, score):
        new_score = Node(name, score)

        if self.head is None:
            self.head = new_score
        else:
            current_score = self.head
            while current_score.next is not None:
                current_score = current_score.next
            current_score.next = new_score
        print('\nAdded Score Success..')

    def search_score(self, name):
        current_score = self.head
        while current_score is not None:
            if current_score.name == name:
                return print("{}'s Score {}".format(name, current_score.score))
            current_score = current_score.next
        return None

    def remove_score(self, name):
        if self.head is None:
            return print('\nScore Empty')

        if self.head.name == name:
            self.head = self.head.next
            return

        current_score = self.head
        while current_score.next is not None:
            if current_score.next.name == name:
                current_score.next = current_score.next.next
                return
            current_score = current_score.next
        print('\nDeleted Score Success..')

    def print_scores(self):
        current_score = self.head
        i = 1
        while current_score is not None:
            print("{}. Name: {}, Score: {}".format(i, current_score.name, current_score.score))
            i += 1
            current_score = current_score.next

scores = LinkedList()
while True:
    print("\nMENU")
    print("1. ADD SCORE")
    print("2. SEARCH SCORE BY NAME")
    print("3. DELETE SCORE BY NAME")
    print("4. LIST SCORE")
    print("5. EXIT")
    choice = int(input("INSERT YOUR CHOICE: "))

    if choice == 1:
        name = input("Name Student: ")
        score = input("Score: ")
        scores.add_score(name, score)
    elif choice == 2:
        name = input("Name Student: ")
        scores.search_score(name)
    elif choice == 3:
        name = input("Name Student: ")
        scores.remove_score(name)
    elif choice == 4:
        print('\nLIST SCORES:')
        scores.print_scores()
    else:
        print("\nTHANKS FOR USING OUR APP")
        exit()
