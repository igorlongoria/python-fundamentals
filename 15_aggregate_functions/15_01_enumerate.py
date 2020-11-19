'''
Demonstrate the use of the .enumerate() function.
'''

batting_order = ["Mookie Betts", "Andrew Benintendi", "J.D. Martinez", "Xander Bogaerts", "Steve Pearce", "Rafael Devers", "Christian Vazquez", "Jackie Bradley Jr.", "Eduardo Nunez"]

print("The batting order for the 2018 Boston Red Sox was: ")
for i, batting_order in enumerate(batting_order, start= 1):
    print(f"{i}: {batting_order}")
