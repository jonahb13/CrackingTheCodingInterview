"""
1.4 - Palindrome Permutation: Given a string, write a function to check if it is a permutation 
of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. The palindrome does not need to be limited to 
just dictionary words. You can ignore casing and non-letter charactrers.

Time Complexity: O(n)
Space Complexity: O(n)

Author: Jonah Beers
"""

string = 'Tact Coa'
string2 = 'Not a Palindrome Permutation'

def is_palindrome_perm(string):
    char_counts = {}
    string = string.replace(' ', '').lower()
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    num_odds = 0
    for count in char_counts.values():
        if count % 2 != 0 and num_odds == 0:
            num_odds = 1
        elif count % 2 != 0 and num_odds == 1:
            return False
    return True

# Driver
print('"'+string+'"', 'is a permutation of a palindome:', is_palindrome_perm(string))
print('"'+string2+'"', 'is a permutation of a palindome:', is_palindrome_perm(string2))
