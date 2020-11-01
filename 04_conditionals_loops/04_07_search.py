'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
n = 652462
number = 0
while number in range(0, 1000000001):
    if number == n:
        print("Your number is:", number)
        break
    number = number + 1
