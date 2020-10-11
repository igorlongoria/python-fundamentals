'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
name = input("What is your name: ")
name_lower = name.lower()
first_letter = name_lower[0]
sliced_name = name_lower[1:]
pig_latin_name = sliced_name + first_letter + "ay"
pig_latin_name_capital = pig_latin_name.capitalize()
print(pig_latin_name_capital)