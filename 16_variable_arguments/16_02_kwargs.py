'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def baseball_positions(**kwargs):
    for i, p in kwargs.items():
        print(i, p)

baseball_positions(RF = "Right Field", DH = "Designated Hitter", OF = "Outfielder", P = "Pitcher" )

