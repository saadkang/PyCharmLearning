"""
Better understanding the concatenation in python
"""

cityname = "Cary"
event = "Magic Show"
print("Welcome to "+cityname+" and enjoy the "+event)
# The above is also the way we concatenate in java, but in python we can choose a easier way
print("Welcome to %s and enjoy the %s" % (cityname, event))

# Now let's see if we only have one variable that we want to include in the print statement
print("Welcome to %s" %(cityname))
# Since you only have one variable you don't need to include the parenthesis
print("Welcome to %s" % cityname)