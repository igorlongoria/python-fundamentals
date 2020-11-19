'''
Write a script with a function that demonstrates the use of *args.

'''

def baseball_greatest(*args):
    for i in args:
        print(i)
baseball_greatest("Babe Ruth", "David Ortiz", "Ricky Henderson", "Fernando Valenzuela")