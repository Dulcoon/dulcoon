class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
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
    
    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop()
            result.append(current_node.value)
            if current_node.left is None:
                queue.append(current_node.left)
            if current_node.right is None:
                queue.append(current_node.right)
        return result
    
    def dfs_pre_order(self):
        results = []
        def transverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None :
                transverse(current_node.left)
            if current_node.right is not None :
                transverse(current_node.right)
            transverse(self.root)
            return results
        
myTree = BinarySearchTree()
myTree.insert(47)
myTree.insert(21)
myTree.insert(76)
myTree.insert(18)
myTree.insert(27)
myTree.insert(52)
myTree.insert(82)
print(myTree.BFS())