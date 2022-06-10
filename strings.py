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
a_string = 'monty pythons flying circus'


def no_duplicates(a_string):
    string = ""
    lst = sorted(set(a_string))
    for i in lst:
        string += i
    print(string)


def reversed_words(a_string):
    lst = a_string.split(" ")
    lst.reverse()
    print(lst)


def four_char_strings(a_string):
    lst = []
    while a_string:
        chars = a_string[:4:]
        lst.append(chars)
        a_string = a_string.replace(chars, "")
    print(lst)


if __name__ == "__main__":
    print("1. - ", end="")
    no_duplicates(a_string)
    print("2. - ", end="")
    reversed_words(a_string)
    print("3. - ", end="")
    four_char_strings(a_string)