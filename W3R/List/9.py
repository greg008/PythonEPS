"""
9. Write a Python program to clone or copy a list.
"""
import copy

lst = [1,2,3,4]

def cp_shallow(lst):
    return copy.copy(lst)

def cp_deep(lst):
    return copy.deepcopy(lst)

def cp_fastest(lst):
    return lst[:]

cp1 = cp_shallow(lst)
print(lst)
print(cp1)
print(lst == cp1)

cp2 = cp_deep(lst)
print(lst)
print(cp2)
print(lst == cp2)

cp3 = cp_fastest(lst)
print(lst)
print(cp3)
print(lst == cp3)

# original_list = [10, 22, 44, 23, 4]
# new_list = list(original_list)
# print(original_list)
# print(new_list)