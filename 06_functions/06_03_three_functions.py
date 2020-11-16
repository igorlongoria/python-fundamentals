'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def square(x):
    return (x * x)

def sum_squares(a,b,c):
    return(square(a) + square(b) + square(c))
print(sum_squares(4,5,6))

sum_example_1 = (sum_squares(23,34,43))
sum_example_2 = (sum_squares(12,12,64))

def compare_sum_of_squares(sum_1, sum_2):
    if sum_1 > sum_2:
        print("Group 1 is bigger")
    else:
        print("Group 2 is bigger")
    if sum_1 or sum_2 == True:
        print("Igor understands functions now")
compare_sum_of_squares(sum_example_1, sum_example_2 )

