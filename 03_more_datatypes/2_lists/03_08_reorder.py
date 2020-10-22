'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
string = "1,2,3,4,5,6,7,8,9,10"
my_list = string.split(",")
print(my_list)
for i in range (0, len(my_list)):
 #   print("i is: ", i)
 #  print("my list of i is: ", my_list[i])
    my_list[i] = int(my_list[i])
my_list.sort()
even_numbers = my_list[1::2]
odd_numbers = my_list[-2::-2]
reordered_list = even_numbers + odd_numbers
#print(my_list)
#print(*reordered_list, sep = ",")
to_print = ""
for number in reordered_list:
    if number == reordered_list[-1]:
        to_print  += str(number)
    else:
        to_print += str(number) + ","
print(to_print)