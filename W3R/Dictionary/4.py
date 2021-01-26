""" TO DO
4. Write a Python script to check whether a given key already
exists in a dictionary.
"""

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def check_key_exist(dict1, key1):

    if key1 in dict1.keys():
        return True
    return False

print(check_key_exist(dict1, 4))
print(check_key_exist(dict1, 14))

# alternative with get
#     d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60};
#
#     print(d.get(6, 'NotExists'));
#
#     print(d.get(0, 'NotExists'));