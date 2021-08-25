"""
1.6 - String Compression: Implement a method to perform basic string compression using the 
counts of repeated characters. For example, the sxtring aabcccccaaa would become a2b1c5a3. If 
the "compressed" string would not become smaller than the original string, your method should 
return the original string. You can assume the string has only uppercase and lowercase letters (a-z).

Time Complexity: O(n)
Space Complexity: O(n)

Author: Jonah Beers
"""

string = 'aabcccccaaa'
string2 = 'aabbcc'

def compress_string(string):
    if len(string) < 3:
        return string
    curr_char, count = '', 0
    compressed_string = ''
    for char in string:
        if char != curr_char:
            if count != 0:
                compressed_string += (curr_char+str(count))
            curr_char = char
            count = 1
        else:
            count += 1
    compressed_string += (curr_char+str(count))
    if len(compressed_string) == len(string):
        return string
    return compressed_string

# Driver
print('The compressed string for', string, 'is:', compress_string(string))
print('The compressed string for', string2, 'is:', compress_string(string2))
