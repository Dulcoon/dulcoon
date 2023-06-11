# bsf menggunakan queue sebagai pegganti array


class NodeQueue:
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
        new_node = NodeQueue(value)
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

    def length_check(self):
        return self.length
    
    def peek_first(self):
        return self.first.value
    
    def peek_last(self):
        return self.last.value

class NodeQueueResult:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueResult:
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
        new_node = NodeQueue(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def length_check(self):
        return self.length
    
    def peek_first(self):
        return self.first.value
    
    def peek_last(self):
        return self.last.value
    
class NodeBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = NodeBST(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == self.root.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def BSF(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while(len(queue) > 0):
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def original_BSF(self):
        dataQueue = Queue()
        queueResult = QueueResult()
        dataQueue.enqueue(self.root)
        while(dataQueue.length_check() > 0):
            current_node = dataQueue.peek_first()
            queueResult.enqueue(current_node.value)
            dataQueue.dequeue()
            if current_node.left is not None:
                dataQueue.enqueue(current_node.left)
            if current_node.right is not None:
                dataQueue.enqueue(current_node.right)
        queueResult.print_Queue()


myTree = BinarySearchTree()
myTree.insert(47)
myTree.insert(21)
myTree.insert(76)
myTree.insert(56)
myTree.insert(78)
myTree.original_BSF()
print(myTree.BSF())






            