'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(Sample_list):
  # define the function here
    max_ = max(Sample_list)
    min_ = min(Sample_list)
    average_ = sum(Sample_list) // max_
    sum_ = sum(Sample_list)

    return max_, min_, average_, sum_


# call the function below here
x = stats(example_list)
#ma, mi, avg, su, = x
ma, mi, avg, su, = stats(example_list)
print(ma, mi, avg, su)

def my_max(any_list):
    largest_number = any_list[0]
    for i in any_list:
      if i > largest_number:
        largest_number = i
    return largest_number

print(my_max([34, 356, 33, 456, 123, 97]))
