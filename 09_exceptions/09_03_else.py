'''
Write a script that demonstrates a try/except/else.

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
else:
    print("Thank you for using the calculator.")