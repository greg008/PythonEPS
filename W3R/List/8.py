"""
8. Write a Python program to check a list is empty or not.
"""

lst1 = []
lst2 = [1, 2]

def check_empty(lst):
    if len(lst) == 0:
        return False
    return True

def check_empty_1(lst):
    if not lst:
        return False
    return True

print(check_empty(lst1))
print(check_empty(lst2))

print(check_empty_1(lst1))
print(check_empty_1(lst2))
