'''
Write the necessary code to print the result of the following formula:

	(15.7 * 3.6 - 34.9 * 0.9) / (68.9 - 2.1)

'''

a = 15.7
b = 3.6
c = 34.9
d = .9
e = 68.9
f = 2.1
g = a * b
h = c * d
i = e -f
res = ((g - h) / i)
print (res)
# it can also be written like this:
print (((a * b) - (c * d)) / (e - f))
