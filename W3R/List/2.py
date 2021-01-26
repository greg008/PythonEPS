"""
2. Write a Python program to multiplies all the items in a list.
"""
lst = [1, 3, 5]
def multiplay(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print(multiplay(lst))