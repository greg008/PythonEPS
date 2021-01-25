"""
8. Write a Python function that takes a list of words and returns
the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""

words = 'al a ma kota'

def longest_word(words):
    lst = words.split()
    longest_word = 0
    for i in lst:
        if len(i) > longest_word:
            longest_word = len(i)
    return longest_word

print(longest_word(words))
print(longest_word('PHP Exercises Backend'))

