# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum(l):
    s=0
    for i in l:
        s+=i
    return s
print(calculate_sum([1,2,3,4,5]))