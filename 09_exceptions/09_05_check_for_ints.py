'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
while True:
    try:
        user_input = int(input("Please type an integer: "))
        if user_input/1 == user_input:
         print("input is a number")
        break
    except Exception:
        print(f'Your input is not an integer.')
