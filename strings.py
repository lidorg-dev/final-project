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

def no_duplicates(a_string):
    sort = ""
    for word in a_string:
        if word == "":
            sort = sort-word
        if word not in sort:
            sort = sort+word
    new = sorted(sort)
    test=''.join(new)
    print(test)
    pass


def reversed_words(a_string):
    newstring = a_string.split()
    reversed = newstring[::-1]
    print(reversed)
    pass


def four_char_strings(a_string):
    length = len(a_string)
    i = 0
    templist = ''
    newlist = []
    while i!=length:
        templist = templist+a_string[i]
        i += 1
        if i % 4 == 0:
            newlist.append(templist)
            templist = ''
    newlist.append(templist)
    print(newlist)
    pass


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

no_duplicates('monty pythons flying circus')
reversed_words('monty pythons flying circus')
four_char_strings('monty pythons flying circus')
