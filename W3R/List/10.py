"""
10. Write a Python program to find the list of words that are longer
 than n from a given list of words.
"""

def long_words(n, lst):
    new_lst = []
    res = lst.split()
    for i in res:
        if len(i) > n:
            new_lst.append(i)
    return new_lst

def long_words_filter(n, lst):
    res = lst.split()
    return list(filter(lambda x: len(x) > n, res))



print(long_words(3, "The quick brown fox jumps over the lazy dog"))
print(long_words_filter(3, "The quick brown fox jumps over the lazy dog"))