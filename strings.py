"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import chunk

import pytest


def no_duplicates(a_string):
    return list(dict.fromkeys(a_string))
mylist = no_duplicates ("monty""pythons""flying""circus")
print("1)",mylist)


def reversed_words(a_string):
    words = a_string.split(' ')
    reverse_a_string = ' '.join(reversed(words))
    return reverse_a_string


if __name__ == "__main__":
    list = 'monty pythons flying circus'
    print("2)",reversed_words(list))


def four_char_strings(a_string, chunk):
    lst = []
    if chunk <= len(a_string):
        lst.extend([a_string[:chunk]])
        lst.extend(four_char_strings(a_string[chunk:], chunk,))
    return lst


a_string = "monty pythons flying circus"
print("3)",four_char_strings(a_string, 4))

#



 #
#
# def test_no_duplicates():
#     s = 'monty pythons flying circus'
#     assert no_duplicates(s) == ' cfghilmnoprstuy'
#
#
# def test_reversed_words():
#     s = 'monty pythons flying circus'
#     assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']
#
#
# def test_four_char_strings():
#     s = 'monty pythons flying circus'
#     assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
#
#
# def main():
# return pytest.main(__file__)


# if __name__ == '__main__':
#  main()
