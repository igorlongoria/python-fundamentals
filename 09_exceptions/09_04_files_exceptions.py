'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
#Instructions are incomplete and confusing. I did what I could.
import os

with open('war_and_peace.txt', 'r') as book1:
    book_1 = list(book1.readline())
    print(book_1[0])
with open('pride_and_prejudice.txt', 'r') as book2:
    book_2 = list(book2.readline())
    print(book_2[0])
with open('crime_and_punishment.txt', 'w') as book3:
    book3.write("")

for dirpath, dirnames, files in os.walk('books'):
    print(f'Found directory: {dirpath}')
    print(f"{dirnames}, files is {files}")
    for file_name in files:
        print(file_name)

        full_file_name = os.path.join(dirpath, file_name)
        print(full_file_name)
        with open(full_file_name, 'r') as book:
            first_line = list(book.readline())
            print(first_line[0])

