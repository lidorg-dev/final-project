"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

"""


def reverseWords(input):


    inputWords = input.split(" ")


    inputWords=inputWords[-1::-1]


    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = 'monty pythons flying circus'
    print (reverseWords(input))
#
Word = "monty pythons flying circus"
print([Word[i:i+4] for i in range(0, len(Word), 4)])
