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
    
    def MinValueNode(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode
    
    def MaxValueNode(self, currentNode):
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode

    
    def totalSelisihKuadrat(self, node):
        if node is None:
            return 0
        return ((node.value - self.get_average(self))**2) + ((self.totalSelisihKuadrat(node.left) - self.get_average(self))**2)  + ((self.totalSelisihKuadrat(node.right) - self.get_average(self))**2)
   
    def get_sum(self, node):
        if node is None:
            return 0
        return node.value + self.get_sum(node.left) + self.get_sum(node.right)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def AverageValue(self):
        sum_values = self.get_sum(self.root)
        num_nodes = self.count_nodes(self.root)
        if num_nodes == 0:
            return 0
        return sum_values / num_nodes
    
    def standarDevasi(self, value):
        temp = self.root
        rootVal = (self.root.value - self.get_average(self))**2
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
                selisihKiri = (temp.value - self.get_average(self))**2
            elif value > temp.value:
                temp = temp.right
                selisihKanan = temp.value - self.get_average(self)
        return rootVal + selisihKiri + selisihKanan
        
    

        

myTree = BinarySearchTree()
myTree.insert(47)
myTree.insert(21)
myTree.insert(76)




# print("Minimum Value in My Tree")
# print(myTree.MinValueNode(myTree.root).value)

# print("Maximum Value in My Tree")
# print(myTree.MaxValueNode(myTree.root).value)

# print("AVG")
# print(myTree.get_average())


# print("BST Contains 27 : ")
# print(myTree.contains(27))

# print("BST Contains 17 : ")
# print(myTree.contains(17))

# print("Root", myTree.root.value)
# print("Root -> Left : ", myTree.root.left.value)
# print("Root -> Right : ", myTree.root.right.value)


            