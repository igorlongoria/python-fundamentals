'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# input = "hello world"
# list_ = input.split()
# # a = tuple(list_[0])
# # b = tuple(list_[1])
# # to_print = a, b
# # final = list(to_print)
# # print(final)
# print(list_)
# to_print = []
# for item in list_:
#     to_print.append(tuple(item))
# print(to_print)

def first_function(input):
    list_ = input.split()
    to_print = []
    for item in list_:
        to_print.append(tuple(item))
    return to_print
a = first_function("Hello my name is Igor")
print(a)


#a = list_[0]
#b = list_[1]
#a = tuple(a)
#b = tuple(b)
#print (input)
