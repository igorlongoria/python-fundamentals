'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(a,b,c,d,e):
    return [a,b,c,d,e]

for i, c in enumerate(my_enumerate(1,2,3,4,5), start= 1):
    print(f"{i}: {c}")
#

#Quiz Code
my_list = ["apple", "banana", "orange"]
x = []
obj1 = enumerate(my_list)
#for i in obj1:
#   x.append(i)
#print(x)
x = ([name for name in obj1])
print(x)
