"""
1. Write a Python script to sort (ascending and descending)
 a dictionary by value.
"""
import operator
dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
def sort_dict(dict1):
    sorted_asc = dict(sorted(dict1.items(), key=operator.itemgetter(1)))
    # sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
    sorted_des = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)

    print(sorted_asc)
    print(sorted_des)

sort_dict(dict1)
