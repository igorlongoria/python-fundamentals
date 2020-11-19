'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
x = [1111, 2222, 3333, 5738, 4932, 4444, 5555, 83838]

gen = (i for i in x)
print(gen)

for i in gen:
    if i % 1111 == 0:
        num = i // 1111
        print(num)