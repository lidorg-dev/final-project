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

my_sl ='monty pythons flying circus'
def no_duplicates(a_string):
    
    result = "".join(dict.fromkeys(my_sl))
    return("".join(sorted(result)))
    



def reversed_words(a_string):
    for i in a_string.split()[::-1]:
        return i


def four_char_strings(a_string):
    c=[]
    i=0
    hold=""

    for letter in a_string:
        i+=1
        hold+=letter

        if i%4==0:
            c.append(hold)
            hold=""

    c.append(hold)

    if hold=="":
        print(c)

    else:
        if hold==c[-1]:
            print(c)

        else:
            c.append(hold)
            print(c)
    
    return c



def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
