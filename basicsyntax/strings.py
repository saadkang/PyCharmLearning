""" Examples to show how String works in python

Sequence of Characters
Can contain letters(a-z), numbers(0-9), and any kind of special character
"""

a = "This is a simple String using double quotes"
b = 'This is a simple String using single quotes'
print(a)
print(b)

# Now let's say we want to using a quote inside a String, how do we do that?

c = "There is a single 'quote' inside a double 'quote' String"
print(c)

d = 'There is a double "quote" inside a single "quote" String'
print(d)

# Now let's try to have a single quote or double quote inside a like quote
"""You can use \ which suppresses the functionality of the of anything that follows that"""
e = "This is a double \"quote\" inside a double \"quote\" String"
print(e)

f = 'This is a single \'quote\' inside a single \'quote\' String'
print(f)

"""Also another common use for \ is if you have a long String and you want to print everything in one line you can
print it in one line by using \ 
"""

g = "This is going to be a really long String\
 but it will be printing everything in one line"
print(g)