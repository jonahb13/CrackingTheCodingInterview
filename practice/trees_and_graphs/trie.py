"""
Trie (Prefix Tree)

Tries can check if a word is valid in O(k), where k is the length of the string.
This is similar runtime to a hash table.
"""

class TrieNode:
    
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode('')
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        
    def dfs(self, node: TrieNode, prefix):
        if node.is_end:
            self.output.append((prefix + node.char)) 
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
            
    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.output = []
        self.dfs(node, word[:-1])
        return self.output
    
# Driver
trie = Trie()
trie.insert('here')
trie.insert('hear')
trie.insert('he')
trie.insert('hello')
trie.insert('how')
trie.insert('hoe')
trie.insert('her')
trie.insert('hi')
trie.insert('hill')
print('Words starting with "he":', trie.search('he'))
print('Words starting with "her":', trie.search('her'))
print('Words starting with "help":', trie.search('help'))