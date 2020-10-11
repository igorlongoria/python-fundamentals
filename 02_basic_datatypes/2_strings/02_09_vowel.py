'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
string = input("Please enter the name of your favorite team: ")
x = string.lower()
a = (x.count("a"))
e = (x.count("e"))
i = (x.count("i"))
o = (x.count("o"))
u = (x.count("u"))
vowels_count = a + e + i + o + u
print("The number of vowels in your team is: ", vowels_count)

# Challenge

x = string.lower()
a = (x.count("a"))
e = (x.count("e"))
i = (x.count("i"))
o = (x.count("o"))
u = (x.count("u"))
vowels_count = a + e + i + o + u
print("The number of a's is: ", a,)
print("The number of e's is: ", e,)
print("The number of i's is: ", i,)
print("The number of o's is: ", o,)
print("The number of u's is: ", u,)