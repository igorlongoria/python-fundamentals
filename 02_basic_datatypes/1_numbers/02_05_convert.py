'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# Convert an int to a float
a = 5
print(a, type(a))
a = float(a)
print(a, type(a))

# Convert float to an int
b = 5.1
print(b, type(b))
b = int(b)
print(b, type(b))

# Perform floor division using a float and an int.
x = 20.5
y = 4
print(x // y)

# Use two user inputted values to perform multiplication.

x = int(input("Please enter a number from 1 to 10: "))
y = int(input("Please enter a number from 11 to 20: "))
print(x, 'times', y, '=', x * y)