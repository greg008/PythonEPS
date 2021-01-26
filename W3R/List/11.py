"""
11. Write a Python function that takes two lists and returns True if they
 have at least one common member.
"""

lst1 = [1,2,3]
lst2 = [6, 4, 5]

def common_mem(lst1, lst2):
    return bool(set(lst1) & set(lst2))

print(common_mem(lst1, lst2))


