"""
10. Write a Python program to sum all the items in a dictionary.
"""
my_dict = {'data1':100,'data2':-54,'data3':247}

def sum_items(my_dict):
    return sum(my_dict.values())

print(sum_items(my_dict))