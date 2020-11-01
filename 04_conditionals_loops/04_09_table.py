'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
my_list = list(range(50))
first_row = ""
second_row = ""
third_row = ""
fourth_row = ""
fifth_row = ""
for number in my_list:
    if number < 10:
        first_row += str(number) + " "
    elif number < 20:
        second_row += str(number) + " "
    elif number < 30:
        third_row += str(number) + " "
    elif number < 40:
        fourth_row += str(number) + " "
    else:
        fifth_row += str(number) + " "

print(first_row)
print(second_row)
print(third_row)
print(fourth_row)
print(fifth_row)