"""
4. Write a Python program to get the smallest number from a list.
"""

lst = [1, 3, 5]
def smallest_num(lst):
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_num(lst))