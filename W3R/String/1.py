"""
Write a Python program to calculate the length of a string.
"""
str1 = "w3resource.com"

print(len(str1))


def string_lenght(str1):
    count = 0
    for i in str1:
        count += 1
    return count

print(string_lenght(str1))
