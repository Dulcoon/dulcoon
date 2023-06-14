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
        
    
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.SKU:
                temp = temp.left
            elif value > temp.SKU:
                temp = temp.right
            else:
                return True
        return False
    
    def find_node_path(self, value):
        if self.root is None:
            return False

        def traverse(current_node, path):
            if current_node is None:
                return False

            if current_node.value == value:
                return True, path

            left_path = path + "-left"
            right_path = path + "-right"

            left_result = traverse(current_node.left, left_path)
            if left_result:
                return left_result

            right_result = traverse(current_node.right, right_path)
            if right_result:
                return right_result

            return False

        result = traverse(self.root, "Root")
        if result:
            return result[1]
        else:
            return "Node tidak ada"
    
        
myTree = BinarySearchTree()
myTree.insert(49)
myTree.insert(28)
myTree.insert(5)
myTree.insert(44)
myTree.insert(50)
myTree.insert(58)
myTree.insert(21)
myTree.insert(66)
myTree.insert(90)
myTree.insert(87)
myTree.insert(42)
myTree.insert(62)
myTree.insert(7)
myTree.insert(24)
myTree.insert(65)
print(myTree.BFS(7))