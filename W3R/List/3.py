"""
3. Write a Python program to get the largest number from a list.
"""

lst = [1, 3, 5]
def largest_num(lst):
    larg = lst[0]
    for i in lst:
        if i > larg:
            larg = i
    return larg

print(largest_num(lst))