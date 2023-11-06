# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_average(numbers):
     total = sum(numbers)
     count = len(numbers)
     average = total / count
     return average
print(calculate_average([1,7,8,9,6]))