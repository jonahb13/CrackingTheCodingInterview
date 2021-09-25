"""
1.9 - String Rotation: Assume you have a method isSubstring which checks if one
word is a substring of another. Given two strings, s1 and s2, write code to check 
if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle"
is a rotation of "erbottlewat").

Time Complexity: O(n)
Space Complexity: O(n)

Author: Jonah Beers
"""

s1 = 'waterbottle'
s2 = 'erbottlewat'

s3 = 'rotation'
s4 = 'ationro'

def is_substring(s1, s2):
    return s2 in s1
    
def is_rotation(s1, s2):
    str_len = len(s1)
    if str_len == len(s2) and str_len > 0:
        return is_substring(s1+s1, s2)
    return False

# Driver
print('Is "' + s2 + '" a string rotation of "' + s1 + '"?', end=' ')
print("Yes" if is_rotation(s1, s2) else "No")
print('Is "' + s4 + '" a string rotation of "' + s3 + '"?', end=' ')
print("Yes" if is_rotation(s4, s3) else "No")