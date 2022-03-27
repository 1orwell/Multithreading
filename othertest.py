import doctest
from operator import is_
from tkinter import W

def fizz_buzz(numbers):
    """ 
    >>> numbers = [45, 22, 15, 39, 10]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 'fizzbuzz', 'fizz', 'buzz']
    """ 

    for i in enumerate(numbers):
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'
        elif num % 3 == 0:
            numbers[i] = 'fizz'
        elif num % 5 == 0:
            numbers[i] = 'buzz'

if __name__ == "__main__":
    doctest.testmod()

lst = [1, 2, 3, 4, -5]

def square(x):
    return x * x

print("using maps")
sqr_list = list(map(square, lst))

print(sqr_list)

# Most "pythonic way"
print("using list comprehension")
print([square(num) for num in lst])

def is_odd(x):
    return x % 2 == 1

print("Using filter to apply is_odd to list")
print(list(filter(is_odd, lst)))

print("Filtering using list comprehension")
print([num for num in lst if is_odd(num)])

# Create 2x3 0 grid

num_rows = 2
num_cols = 3
grid = []

for _ in range(num_rows):
    curr_row = []
    for _ in range(num_cols):
        curr_row.append(0)
    grid.append(curr_row)

print(grid)

print("Creating grid using list comp")

grid_comp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
print(grid_comp)

print("Finding max square of list")
print(max(lst, key = lambda x: x*x))

print(max(map(lambda x:x*x, lst)))

# any([True, False]) = True
# any([False, False]) = False

#any(lst, key = lambda x: x%2==1)
# The above doesn't work as any does not take a key arguement, use list comp instead

print("Using list comp to check values in list are true or false")
print([num for num in lst if num%2 == 1])

print("Return bool for if num is even or odd")
print("List is" + str(lst))
bool_lst = [(lambda x: x%2==1)(num) for num in lst]
print(any(bool_lst))
print(all(bool_lst))