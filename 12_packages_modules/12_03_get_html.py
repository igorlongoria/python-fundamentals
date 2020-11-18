'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''
# I installed the requests module in my terminal.
import requests

x = requests.get("https://codingnomads.co/online-coding-bootcamp-mentorship")

print(x.text)