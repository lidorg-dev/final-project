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

def no_duplicates():
    str = 'monty pythons flying circus'
    remove = ''.join(sorted(set(str), key=str.index))
    sort = ''.join(sorted(remove))
    print(sort)
no_duplicates()
pass

def reversed_words(sentence):
    # first split the string into words
    words = sentence.split(' ')
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))
    # finally return the joined string
    return reverse_sentence
if __name__ == "__main__":
    input = 'monty pythons flying circus'
    print(reversed_words(input))
pass

def four_char_strings():
    str1 = ['monty', 'pythons', 'flying', 'circus']
    for i in str1:
        print(i[:4])
four_char_strings()
pass
