'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
def first_function(number):
    if number %4 == 0 or number %7 == 0:
        return True
    else:
        return False

print(first_function(35))

def second_function(number):
    if number %4 == 0 and number %7 == 0:
        return True
    else:
        return False

print((second_function(24)))

first_function(40)