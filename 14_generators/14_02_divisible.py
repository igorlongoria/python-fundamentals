'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
x = [1111, 2222, 3333, 5738, 4932, 4444, 5555, 83838]

gen = (i for i in x)
print(gen)

for i in gen:
    if i % 1111 == 0:
        print(i)