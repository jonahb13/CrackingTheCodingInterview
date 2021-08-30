"""
Hash Table

Average time complexity for insert, get, delete: O(1), worst case being O(n)
"""

class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    

class HashTable:
    
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity
        
    def __str__(self):
        string = '{'
        for bucket in self.table:
            if bucket is not None:
                node = bucket
                string += (str(node.key) + ': ' + str(node.value) + ', ')
                while node.next is not None:
                    node = node.next
                    string += (str(node.key) + ': ' + str(node.value) + ', ')
        return string[:-2] + '}'
    
    def __repr__(self):
        return str(self)
        
    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
        else:
            while node is not None:
                prev = node
                node = node.next
            prev.next = Node(key, value)
        self.size += 1
        
    def delete(self, key):
        index = self.hash(key)
        node = self.table[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        if prev is None:
            self.table[index] = node.next
        else:
            prev.next = prev.next.next
        self.size -= 1
        
    def get(self, key):
        index = self.hash(key)
        node = self.table[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        return node.value
    
# Driver
scores = HashTable()
scores.insert('sam', 7)
scores.insert('jacob', 3)
scores.insert('mary', 6)
scores.insert('jeremy', 2)
scores.insert('jreemy', 3)
print(scores)
scores.delete('jreemy')
print(scores)
        