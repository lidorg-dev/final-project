import pytest


def no_duplicates(a_string):
    try:
     sorted_string = ''.join(sorted(set(a_string)))
     print(sorted_string)
     return sorted_string
    except:
        print("The string was not found")

def reversed_words(a_string):
    words = a_string.split()
    reversed_words = words[::-1]
    print(reversed_words)
    return reversed_words

def four_char_strings(a_string):
    strings = []
    for i in range(0, len(a_string), 4):
        string = a_string[i:i+4]
        if len(string) == 4:
            strings.append(string)
        #This for the end of the string that will be added even though it is equal to 3
        else:
            strings.append(string)
    print(strings)
    return strings

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

string = 'monty pythons flying circus'
no_duplicates(string)
reversed_words(string)
four_char_strings(string)
