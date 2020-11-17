'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'

#with open('integers.txt', 'r') as book:
try:
    with open('integers.txt', 'r') as book:
        first_number = int(book.readline())
except IOError as IO:
        print("There is an error in the input of your file.", IO)
except ValueError as VE:
        print("The first number of the text is not an integer.", VE)
else:
    print(first_number * 5)