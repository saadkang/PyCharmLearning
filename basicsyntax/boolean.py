"""Showing how boolean works in python"""

a = True
b = False

# Remember in python whenever you write down 'true' or 'false' 'T' and 'F' must be capital

print(a)
print(b)
print('You can express true or false in numbers to: so 0 is false and everything else is true')

print(bool(0))
print(bool(1))

# Like the one I'm about to do here, boolean of a non-zero number is true

print(bool(2))

# In python null is none: meaning just double quote and nothing in between them not even space
c = ""
print(bool(c))

# Now, let's give c variable a value and then check the bool status
c = "Some Value"
print(bool(c))
# So we discovered that nothing is FALSE, but if there is some value to a variable then it is TRUE
