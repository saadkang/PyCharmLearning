"""Like java there are some keywords that you can't use in the python as well"""

import keyword
"""By using the line below, you will know which words you can't use to name a variable"""

print(keyword.kwlist)

"""A variable name can only have letters, numbers, and underscore no special characters"""

"""Now if we have to assign a value to multiple variables we can do that like so"""
a = b = c = 10
print(a)
print(b)
print(c)

"""And if we need to have few lines of code we can assign different values to different variables"""
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)