"""
2.3 - Delete Middle Node: Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the exact middle) 
of a singly linked list, given only access to that node.

Time Complexity: O(1)
Space Complexity: O(1)

Author: Jonah Beers
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
   
   
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def add(self, data):
        node = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node
        return node
 
    def delete_node(self, node: Node):
        node.data = node.next.data
        node.next = node.next.next
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next

# Driver
nodes = LinkedList()
node1 = nodes.add('a')
node2 = nodes.add('b')
node3 = nodes.add('c')
node4 = nodes.add('d')
node5 = nodes.add('e')

print('Linked list:')
nodes.print_list()
nodes.delete_node(node3)
print('\nLinked list after removing "c":')
nodes.print_list()
nodes.delete_node(node2)
print('\nLinked list after removing "b":')
nodes.print_list()
