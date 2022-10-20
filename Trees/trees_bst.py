class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
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
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False  

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
            

b = BinarySearchTree()
b.insert(47)
b.insert(21)
b.insert(76)
b.insert(18)
b.insert(27)
b.insert(52)
b.insert(82)
print(b.min_value_node(b.root.right).value)

