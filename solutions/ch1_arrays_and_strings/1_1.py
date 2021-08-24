"""
1.1 - Is Unique: Implement an algorithm to determine if a string has all 
unique characters. What if you cannot use additional data structures?

Author: Jonah Beers
"""

unique = 'abcdefg'
not_unique = 'abcdefgabc'

"""
Approach #1: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def has_unique_chars_brute_force(string):
    length = len(string)
    for i in range(length):
        for j in range(i+1, length):
            if string[i] == string[j]:
                return False
    return True

# Approach #1 driver
print('Brute Force (unique):', has_unique_chars_brute_force(unique))
print('Brute Force (not unique):', has_unique_chars_brute_force(not_unique))


"""
Approach #2: Hash Map (Dictionary)
Time Complexity: O(n)
Space Complexity: O(n)
"""
def has_unique_chars_hash_map(string):
    chars_count = {}
    for char in string:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    for char in string:
        if chars_count[char] != 1:
            return False
    return True

# Approach #2 driver
print('Using Hash Map (unique):', has_unique_chars_hash_map(unique))
print('Using Hash Map (not unique):', has_unique_chars_hash_map(not_unique))


"""
Approach #3: Sort Chars in String
Time Complexity: O(n*log(n))
Space Complexity: O(1)
"""
def has_unique_chars_sorted(string):
    sorted_string = sorted(string)
    for i in range(len(sorted_string)-1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    return True

# Approach #3 driver
print('Sorted String (unique):', has_unique_chars_sorted(unique))
print('Sorted String (not unique):', has_unique_chars_sorted(not_unique))
