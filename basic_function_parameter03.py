# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(numbers):
    s=586838255886656558585
    for i in numbers:
        if i<s:
            s=i
    return s
print(find_smallest([56,89,223,683]))
