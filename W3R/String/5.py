"""
5. Write a Python program to get a single string from two given strings,
 separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
str_1 = 'abc'
str_2 = 'xyz'

def conc(str_1, str_2):
    return str_2[:2] + str_1[-1] + ' ' + str_1[:2] + str_2[-1]

print(conc(str_1, str_2))

