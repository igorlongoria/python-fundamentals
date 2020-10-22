'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
string = "hello hello also when how for when for week also tomorrow today when also for who how hello when try tomorrow today"
list_ = string.split()
word_count = 0
num = list_[0]

for item in list_:
    most_ocurr = list_.count(item)
    if(most_ocurr > word_count):
        word_count = most_ocurr
        num = item
print(num)
