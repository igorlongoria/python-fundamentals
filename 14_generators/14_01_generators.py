'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gen = (i for i in x)
print(gen)

for i in gen:
    print(i)