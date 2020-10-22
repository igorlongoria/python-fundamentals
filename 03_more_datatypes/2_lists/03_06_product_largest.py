'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
# string =  (input("Type 10 numbers from 1 to 100: "))
string = "1 4 6 2 4 1 456 94 85 20"
list = string.split()
for i in range (0, len(list)):
    list[i] = int(list[i])
list.sort()
print(list)
print(list[-1])

my_list = [13,46,34,744,573,567]
biggest = 0
for num in my_list:
    if num > biggest:
        biggest = num

input_string = "1,2,3,4,5,6,7,8,9"
word = ""
delimiter = ","
my_empty_list = []
for character in input_string:
    if character == delimiter:
        my_empty_list.append(word)
        word = ""
    else:
        word += character
print(my_empty_list)