
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

import pytest

string='monty pythons flying circus'

def no_duplicates(a_string):
    sort=''
    for i in a_string:
        if i != ' ':
            if i not in sort:
                sort = sort + i
    yep = sorted(sort)
    string=''.join(yep)
    return string
    pass


def reversed_words(a_string):
     spl = a_string.split()
     reverse = spl[::-1]
     return reverse
     pass


def four_char_strings(a_string):
    j = 0
    temp = ''
    new_string = []
    print('Start:' + a_string)
    for i in a_string:
        temp = temp + i
        if j == 3:
                new_string.append(temp)
                temp = ''
                j = 0
        else:
            j = j + 1
    new_string.append(temp)
    return new_string

    pass

def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == 'cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']



def main():

    return pytest.main(["strings.py"])

if __name__ == '__main__':
    main()



