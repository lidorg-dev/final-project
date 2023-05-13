import pytest

def no_duplicates(a_string):
    return ''.join(sorted(set(a_string)))


def reversed_words(a_string):
    return a_string.split()[::-1]


def four_char_strings(a_string):
    return [a_string[i:i+4] for i in range(0, len(a_string), 4)]


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
    return pytest.main([__file__])


if __name__ == '__main__':
    main()

