"""
1.5 - One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two strings, 
write a function to check if they are one edit (or zero edits) away.

Time Complexity: O(n)
Space Complexity: O(1)

Author: Jonah Beers
"""

string1, string12 = 'pale', 'pales'
string2, string22 = 'pale',  'ple' 
string3, string32 = 'pale',  'bale'
string4, string42 = 'pale', 'bake'

def is_one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    pointer1, pointer2 = 0, 0
    has_edit = False
    while pointer1 < len(string1) and pointer2 < len(string2):
        if string1[pointer1] == string2[pointer2]:
            pointer1 += 1
            pointer2 += 1
        elif not has_edit:
            if len(string2) > len(string1):
                pointer2 += 1
            elif len(string2) < len(string1):
                pointer1 += 1
            else:
                pointer1 += 1
                pointer2 += 1
            has_edit = True
        else:
            return False
    return True
    
# Driver
print('"'+string1+'"', 'is one away from', '"'+string12+'":', is_one_away(string1, string12))
print('"'+string2+'"', 'is one away from', '"'+string22+'":', is_one_away(string2, string22))
print('"'+string3+'"', 'is one away from', '"'+string32+'":', is_one_away(string3, string32))
print('"'+string4+'"', 'is one away from', '"'+string42+'":', is_one_away(string4, string42))
