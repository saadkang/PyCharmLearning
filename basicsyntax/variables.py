""""
table
object reference count
"""
"""In python you don't have to say the variable type(e.g. String, int, long, boolean, etc) python knows it"""
a = 'nyc'
"""You can use either single quote or double in python it doesn't matter"""
b = "nyc"

print(a)

a = 123
"""So it is common sense that, if you change the value of a variable the memory doesn't remember the old one"""

print(a)
print(b)

c = 456
d = c

"""Line below means 'if c is equal to d' and if the both variables are the same the console
should print out true and vice versa"""

print(c == d)

"""You can say this in a different way, it is the same thing"""

print(d is c)