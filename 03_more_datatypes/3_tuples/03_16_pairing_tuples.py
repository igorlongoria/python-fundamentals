'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
x = [4, 3, 6, 5, 7, 2, 8]
y = sorted(x)
tupe_list = [(x[i], y[i]) for i in range(0,len(x))]
print(tupe_list)

# tuple_list = [(x[0], y[0]), (x[1], y[1])]
# print(tuple_list)
