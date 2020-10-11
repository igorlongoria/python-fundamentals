'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

sentence = input("Please write a sentence: ")
symbol = input("Please write a symbol: ")
first = sentence[0]
print(sentence.replace(first, symbol))
