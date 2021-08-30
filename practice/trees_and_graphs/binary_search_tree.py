"""
Binary Search Tree

Balanced binary search trees have O(log(n)) time complexity for inserting and finding nodes.
"""

class Node:
    
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def get_root(self):
        return self.root
    
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.add_node(data, self.root)
            
    def add_node(self, data, node: Node):
        if data < node.data:
            if node.left is not None:
                self.add_node(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self.add_node(data, node.right)
            else:
                node.right = Node(data)
    
    def find(self, data):
        if self.root is None:
            return None
        else:
            return self.find_node(data, self.root)
        
    def find_node(self, data, node: Node):
        if data == node.data:
            return node
        elif data < node.data and node.left is not None:
            return self.find_node(data, node.left)
        elif data > node.data and node.right is not None:
            return self.find_node(data, node.right)
        
# Driver
tree = BinarySearchTree()
tree.add(4)
tree.add(2)
tree.add(6)
tree.add(1)
tree.add(3)
tree.add(5)
tree.add(7)
        