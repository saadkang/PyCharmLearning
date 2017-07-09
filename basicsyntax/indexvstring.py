"""
We will see how the index works in python
"""

nameOfAString = "This is for educational purposes only"

# The : in the [] is has no starting and ending index so it will print the whole String
print("There is nothing before or after the : so it will print complete String: "+nameOfAString[:])

# In the example below there is a number in front of the : so the starting index is 1
# There is no number after the : so it will print rest of the index
print("There is 1 in front of : and nothing after, so it will start at index 1 and print everything: "+nameOfAString[1:])

# In the example below there is no starting index so it will print all, but there is an ending index
# We learned previously that the ending index is exclusive so that will not get printed
print("There is nothing in front of the : and 9 after, so It will print all the index and stop at 8: "+nameOfAString[:9])

# So the cool this is the index can be started from either side, if you choose to start from the
# right side then the index will starts from -1, -2, -3,..,-37
# So in the example below the -37 is the first index on the far left hand side "T"
print("Numbering index is a circle starting from left is 0, and starting from right is -1: "+nameOfAString[-37])

print("So now I'm trying to put -1:-1 and what to see what prints: "+nameOfAString[-1:-1])
# Nothing printed on the console, I guess the reason for that is, it did start with -1 index which is the starting
# index and then it looked at the ending index which is also -1 and ending index is exclusive so nothing gets printed

# Now let's talk about the skip part
# The second : is for skipping an index, in the example below there is nothing after the : so nothing will be skipped
print(nameOfAString[::])
# The example below is saying to skip nothing so it is the same thing as above
print(nameOfAString[::1])

# This is skipping two index and printing the third one on the console
print(nameOfAString[::3])

# To reverse the String you can just type -1 after the second :
print("Reverse the value of a String and you get: "+nameOfAString[::-1])