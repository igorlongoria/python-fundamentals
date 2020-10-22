'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_1 = list_[3:4]
unique_2 = list_[5:7]
unique_3 = list_[9:]
unique_list = unique_1 + unique_2 + unique_3
print(unique_list)