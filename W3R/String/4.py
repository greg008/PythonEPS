"""
4. TO DO Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$',
 except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

def change_str(string):
    new_string = ""
    for i in range(len(string)):
        if i != 0 and string[i] == string[0]:
            new_string += "$"
        else:
            new_string += string[i]
    return new_string


print(change_str("restart"))