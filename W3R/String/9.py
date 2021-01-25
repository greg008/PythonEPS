"""
9. Write a Python program to remove the nth index character from
a nonempty string.
"""

def rem_nth_char(str1, nth):
    return str1[:nth] + str1[nth+1:]

print(rem_nth_char('Python', 0))
print(rem_nth_char('Python', 3))

