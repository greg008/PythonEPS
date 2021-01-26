"""
5. Write a Python program to count the number of strings
where the string length is 2 or more and the first and last character
are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

lst = ['abc', 'xyz', 'aba', '1221']

def count(lst):
    counter = 0
    for i in lst:
        if len(i) >=2 and i[0] == i[-1]:
            counter += 1
    return counter

print(count(lst))

