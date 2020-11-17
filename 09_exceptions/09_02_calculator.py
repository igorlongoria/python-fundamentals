'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    dividend = int(input("Please enter a number to be divided: "))
    divisor = int(input("Please enter the divisor: "))
    result = dividend / divisor
    print(f'The result is {result}')
except ValueError as ve:
    print("Letters are not numbers, please try again.", ve)
except ZeroDivisionError as zde:
    print("Big mistake.", zde)
