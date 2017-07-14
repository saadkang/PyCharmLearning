"""
Tuple
Like list but they are immutable
that means you can't change them
"""

# What the above line in green is trying to say is that list (also called Array in Java) can be changed
# Like in the example below:
# The list or Array is defined by the []
my_list = [1, 2, 3]
print(my_list)
my_list[0] = 0
print(my_list)
print('*'*40)
# The tuple is immutable so can't be changed and they are defined by ()
my_tuple = (1, 2, 3)
print(my_tuple)
# So if we try to change the index of a tuple we will get the 'assignment not supported' error
# So I'm not going to try that here, just know you can't change it.
# But you can access different index of the tuple
print('*'*40)
print(my_tuple[0])
# And we can also do slicing or skipping with the tuple
print('*'*40)
print(my_tuple[1:])
print('*'*40)
# We can also find out the index of the items in the tuple
# Let's say we want to find out the index of item or data '2' in the tuple
# we can just type it in the print statement
print("The index of the data '2' in the tuple 'my_tuple' is: %s" % my_tuple.index(2))
# The next thing we can do with the tuple is find how many times a entry is repeated in the tuple
print('*'*40)
print("'1' appeared in the tuple 'my_tuple' exactly %s times" % my_tuple.count(1))
# To understand this count() method let's create a new tuple and use it in examples
print('*'*40)
my_second_tuple = (1, 2, 3, 4, 3, 6, 3, 8, 3)
print("'3' appeared in the tuple 'my_second_tuple' exactly %s times" % my_second_tuple.count(3))