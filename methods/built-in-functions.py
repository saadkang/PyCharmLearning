"""
Some built-in functions
max()  --> It takes any number of arguments and returns the largest one.

min()  --> It takes any number of arguments and returns the smallest one.

abs()  --> It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number

type()  --> It returns the type of the data it receives as a argument.
"""

def large_num(*args):
    print(max(args))

large_num(-22, -200, 56, -4567, 67, -4)
print("*" * 40)
# We can write return instead of print, and in the above line we can store that in the variable, and then print that
# variable
def largest_num(*args):
    return max(args)

largest = largest_num(-22, -200, 56, -4567, 67, -4)
print(largest)
print("*" * 40)

# Now, we can do the same thing with the other ones

def smallest_num(*args):
    return min(args)

smallest = smallest_num(-22, -200, 56, -4567, 67, -4)
print(smallest)
print("*" * 40)

# Now working with the absolute value
def abs_num(args):
    print(abs(args))

abs_num(20)
abs_num(-20)
print("*" * 40)

# Now, let's find out the type of each variable
print(type(99))
print(type(99.9))
print(type("99.9"))
# Same way we can find out the type of a list, well we know it is a list because we are defining it and then
# asking for the type, but what if we only have a variable name and then we need to find out about the type of it
l = [1, 2, 3, 4]
print(type(l))