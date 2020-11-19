'''
Using list comprehension, create a list that contains the individual
letters using the word "CodingNomads".

For example:

word = "CodingNomads"
..your code
result_list = ['C', 'o', 'd', 'i', 'n', 'g', 'N', 'o', 'm', 'a', 'd', 's']

'''
word = "CodingNomads"

gen = (letter for letter in word)

print(gen)
for i in gen:
    print(i)
gen = (letter for letter in word)
for i in gen:
    print("done")
    print(i)
    print("done")