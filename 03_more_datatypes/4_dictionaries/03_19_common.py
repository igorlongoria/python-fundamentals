'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
#print(dict_1)
combined = {}
for i in dict_1:
    if i in dict_2:
        dict_1[i] = dict_1[i] + dict_2[i]
for i in dict_2:
    if i not in dict_1:
        dict_1[i] = dict_2[i]
        combined = dict_1
print(combined)