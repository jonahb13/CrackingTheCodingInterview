"""
1.3 - URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the 
additional characters, and that you are given the "true" length of the string.

Author: Jonah Beers
"""

string = 'Mr John Smith    '
string_length = 13
string2 = 'This has been URLified      '
string2_length = 22

"""
Approach #1: Copy Chars to New String
Time Complexity: O(n)
Space Complexity: O(n)
"""
def urlify_copy(string):
    url = ''
    string = string.strip()
    for char in string:
        if char == ' ':
            url += '%20'
        else:
            url += char
    return url

# Approach #1 driver
print('String:', string)
print('URLified string (copied):', urlify_copy(string))
print('String:', string2)
print('URLified string (copied):', urlify_copy(string2))


"""
Approach #2: Modify String As List
Time Complexity: O(n)
Space Complexity: O(1)
"""
def urlify_modify(string, length):
    pointer1 = length - 1
    pointer2 = len(string) - 1
    string = list(string)
    while pointer1 >= 0 and pointer2 >= 0:
        if string[pointer1] == ' ':
            for char in '02%':
                string[pointer2] = char
                pointer2 -= 1
        else:
            string[pointer2] = string[pointer1]
            pointer2 -= 1
        pointer1 -= 1
    string = ''.join(string)
    return string

# Approach #2 driver
print('String:', string)
print('URLified string (modified):', urlify_modify(string, string_length))
print('String:', string2)
print('URLified string (modified):', urlify_modify(string2, string2_length))
