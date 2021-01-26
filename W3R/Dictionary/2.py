"""
2. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""

dict1 = {0: 10, 1: 20}


dict1[2] = 30
# or     
#  dict1.update({2 : 30})

print(dict1)