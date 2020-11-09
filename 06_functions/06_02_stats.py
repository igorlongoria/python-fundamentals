'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  # define the function here
  for i in example_list:
    max_ = max(example_list)
    min_ = min(example_list)
    average_ = sum(example_list) // max_
    sum_ = sum(example_list)
  print(max_, min_, average_, sum_)
  pass

# call the function below here
stats()