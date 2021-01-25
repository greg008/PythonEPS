"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
 If the string length is less than 2, return instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

def create_string(string):
    if len(string) < 2:
        return("")
    return string[:2] + string[-2:]

print(create_string("w3resource"))
print(create_string("w3"))
print(create_string("3"))