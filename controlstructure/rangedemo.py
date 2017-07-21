"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful in generating numbers
"""

# So as we have accomplished in the past that whenever we are giving the range of numbers the lower limit in inclusive
# but the higher limit of the range is exclusive
print(list(range(0, 10)))
print('*'*40)
# The print out of the above line is just going to give you all the numbers that are included in the range
# Typing 'print(range(0, 10))' will print 'range(1, 10)' on the console it will not show the numbers inside the range
# We have to assign it to the list() method


# We can do all these thing in a different approach, by first defining the variable and then use that in the print
# statement instead of the using 'range(x, x)' every single time
num_1 = range(0, 10)
print(num_1)
# Typing just the above will not give the items of the range, it will only tell you what the range is
print(list(num_1))
print('*'*40)


# Similarly we can find out the type of the range
print(type(num_1))
# For this particular example the console will display, '<class 'range'>' meaning 'num' is a class and type of that
# class is 'range'
print('*'*40)


# The starting point of the range is '0' by default so if I want the range to start from '0' I don't have to mention it
num_2 = range(20)
print(list(num_2))
print('*'*40)
# In the above example we didn't set the starting point but we mention the ending point and again the number '20'
# is exclusive, the console shows the range from '0' all the way to '19'


# There are more parameters for 'range', the next one are about to talk about is 'STEP' meaning do we want to print
# out for all the numbers in the range or we want to skip a step, let's look at the example for more details
# By default the value of 'STEP' is '1'
num_3 = range(10, 20, 2)
print(list(num_3))
print('*'*40)
# So I learned an important piece of information, when we are using the 'STEP' we have to mention the starting point
# of the 'range'

# The most important use of 'range' is in the For loop
num_4 = [1, 2, 3]
for l in num_4:
    print(l)
print('*'*40)


# We don't have to define the 'list' and we can still print out the layout or same output of the 'list' using the
# For loop
for cat in range(1, 4):
    print(cat)