'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
first_name = input("Plese enter your first name: ")
middle_name = input("Please enter your middle name: ")
last_name = input("Please enter your last name: ")
comma = ","
x = len(first_name)
y = len(middle_name)
z = len(last_name)
print(x, ",", first_name)
print(y,",", middle_name)
print(z,",", last_name)

string_list = [first_name, middle_name, last_name]
res = max(string_list, key = len)
print("The longest string in your name is: ", res)