'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        We get a syntax error.
        * How helpful are the error messages?
Very helpful as it identifies the problem to be solved
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.

'''
print("Hello world")
help('print')
print(2+2)
# Seconds in a year formula below
days = 365.25
hours_in_a_day = 24
minutes_in_an_hour = 60
second_in_a_minute = 60
seconds_in_a_year = (days * hours_in_a_day * minutes_in_an_hour * second_in_a_minute)
z = seconds_in_a_year
x = "There are"
y = "seconds in a year"
print(x, z, y)