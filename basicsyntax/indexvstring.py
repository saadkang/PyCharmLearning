"""
We will see how the index works in python
"""

nameOfAString = "This is for educational purposes only"

# The : in the [] is has no starting and ending index so it will print the whole String
print(nameOfAString[:])

# In the example below there is a number infront of the : so the starting index is 1
# There is no number after the : so it will print rest of the index
print(nameOfAString[1:])

# In the example below there is no starting index so it will print all, but there is an ending index
# We learned previously that the ending index is exclusive so that will not get printed
print(nameOfAString[:9])

# So the cool this is the index can be started from either side, if you choose to start from the
# right side then the index will starts from -1, -2, -3,..,-37
# So in the example below the -37 is the first index on the far left hand side "T"
print(nameOfAString[-37])