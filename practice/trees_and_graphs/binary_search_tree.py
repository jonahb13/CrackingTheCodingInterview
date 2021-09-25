"""
Binary Search Tree

Balanced binary search trees have O(log(n)) time complexity for inserting and finding nodes.
(This is not a self balancing binary search tree, so worst case is O(n))
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
                
    def in_order_traversal(self, node: Node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)
    
    def pre_order_traversal(self, node: Node):
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node: Node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")
    
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
print('In-Order Traversal of tree:', end=' ') 
tree.in_order_traversal(tree.root)
print('\nPre-Order Traversal of tree:', end=' ')
tree.pre_order_traversal(tree.root)
print('\nPost-Order Traversal of tree:', end=' ')
tree.post_order_traversal(tree.root)