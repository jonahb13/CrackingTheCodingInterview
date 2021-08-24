"""
1.2 - Check Permutation: Given two strings, write a method to
decide if one is a permutation of the other.

Author: Jonah Beers
"""

permutation_string1 = 'qwerty'
permutation_string2 = 'erwtqy'

not_permutation_string1 = 'qwerty'
not_permutation_string2 = 'erwtqi'

"""
Approach #1: Sort Chars in Strings
Time Complexity: O(n*log(n))
Space Complexity: O(1)
"""
def check_permutation_sorted(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)
    if str1_length != str2_length:
        return False
    str1_sorted = ''.join(sorted(str1))
    str2_sorted = ''.join(sorted(str2))
    for i in range(str1_length):
        if str1_sorted[i] != str2_sorted[i]:
            return False
    return True
    
# Approach #1 driver
print('Sorted Strings (permutation):', check_permutation_sorted(permutation_string1, permutation_string2))
print('Sorted Strings (not permutation):', check_permutation_sorted(not_permutation_string1, not_permutation_string2))


"""
Approach #2: Hash Map (Dictionary)
Time Complexity: O(n)
Space Complexity: O(n)
"""
def check_permutation_hash_map(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)
    if str1_length != str2_length:
        return False
    chars_counts = {}
    for char in str1:
        if char in chars_counts:
            chars_counts[char] += 1
        else:
            chars_counts[char] = 1
    for char in str2:
        if char in chars_counts:
            chars_counts[char] -= 1
        else:
            chars_counts[char] = 1
    return all(count == 0 for count in chars_counts.values())
    
# Approach #2 driver
print('Using Hash Map (permutation):', check_permutation_hash_map(permutation_string1, permutation_string2))
print('Using Hash Map (not permutation):', check_permutation_hash_map(not_permutation_string1, not_permutation_string2))
