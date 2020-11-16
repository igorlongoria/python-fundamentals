'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
words = []
with open('words.txt', 'r') as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)
#    print(words)

shortest_length = 99999
for w in words:
    if len(w) < shortest_length:
        shortest_length = len(w)
        for j in words:
            if len(j) == len(w):
             print(j)

count = 0
for item in words:
    if len(item) > count:
        count = len(item)
        longest_word = item
for h in words:
    if len(h) == len(longest_word):
        print(h)

