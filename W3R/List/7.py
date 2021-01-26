"""
7. Write a Python program to remove duplicates from a list.
"""
lst = [10,20,30,20,10,50,60,40,80,50,40]

def rem_duplicate(lst):
    return list(set(lst))

print(rem_duplicate(lst))

def rem_duplicate_1(lst):
    # return dict.fromkeys(lst)
    return list(dict.fromkeys(lst))

print(rem_duplicate_1(lst))