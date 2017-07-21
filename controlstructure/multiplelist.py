"""
Iteration multiple list at the same time
"""

# We can use the iterator with multiple list at the same time
# Let's say we have two list and we want to iterate them
# What iterate does is print the items of the list in pairs so it will stop when the shortest list is finished
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8, 9, 10]
for a, b in zip(list_1, list_2):
    print(a)
    print(b)
print('*'*40)
# There is a built-in function call zip() it is more of a method, as you can see in the console that it stopped print
# out the items of both of the list when the shorter list was ended


# There are more functions that we can add to the iterator, more like conditions
for a, b in zip(list_1, list_2):
    if a > b:
        print(a)
    else:
        print(b)
print('*' * 40)
# This is just a simple condition that was applied that if a > b then print the item of list_1 otherwise or else print
# the item of list_2


# Let's see if it will work with three list at a time
list_3 = [11, 12, 13, 14, 15, 16, 17]
for a, b, c in zip(list_1, list_2, list_3):
    print(a)
    print(b)
    print(c)
# So, as you can see in the console that it did work with three list as well so that proves it that we can have as
# many list as we want and the iterator will work with that too