"""
6. Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends with 'ing'
then add 'ly' instead. If the string length of the given string is less than 3,
 leave it unchanged.

Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

def add_ing(str1):
    if len(str1) > 3:
        if str1.endswith('ing'):
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1

print(add_ing('string'))
print(add_ing('abc'))
print(add_ing('ac'))



