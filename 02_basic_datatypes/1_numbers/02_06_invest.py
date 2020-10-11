'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
i = int(input("Please enter investment amount: "))
r = int(input("please enter rate in percentage: "))
n = int(input("Please enter number of years to invest: "))
fv = i * (1+r/100) ** n
print(fv)
