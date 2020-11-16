'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
words = []

with open('words.txt', 'r') as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

words_reverse = []
for i in words[::-1]:
    words_reverse.append(i)
print(words_reverse)
with open("words_reverse.txt", "w") as my_text:
    my_text.write("\n".join(words_reverse))

# while True:
#     last_word = words[-1]
#     words_reverse.append(last_word)
#     words.remove(last_word)
# print(words_reverse)

# print(last_word)
# words.remove(last_word)
# last_word = words[-1]
# print(last_word)