"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

# Enclosing loop meaning nested loop
x = 0
while x < 10:
    print("The value of x is: "+str(x))
    x = x + 1
print('*'*40)
print('*'*40)
print('*'*40)
# So since Python doesn't have brackets and everything is depending on the indentation, so you can write lines in
# different order, and still be ok to run
# For example:
y = 0
while y < 10:
    print("The value of y is: "+str(y))
    y = y + 1

    if y == 8:
        break
    print("This line can be written some place else")
    print("*"*40)
print('*'*40)
print('*'*40)
print('*'*40)
# Now I let's try a different approach of doing the same thing as above
z = 0
while z < 10:
    print("The value of z is: "+str(z))
    z = z + 1
    print("This is the same line now, at a different place")
    print('*' * 40)
    if z == 8:
        break
# But there is more to lines and order, the loops and nested loops are going line by line, but it also consider what
# is the order of the lines I know it is confusing but it will make sense soon
# Let's try and use the 'continue' instead of 'break' to understand it better
a = 0
while a < 10:
    print("This is from the variable a: "+str(a))
    a = a + 1

    if a == 8:
        continue
    print("This is variable a")
    print('*'*40)
# So when the loop was running with '7' as a's value it hit 'if' loop and the 'if' loop was saying continue, what
# continue does is skip whatever is written after that and starts the loop from the beginning
# To be honest I have no idea what is the use of it but it doesn't hurt to learn this

# One most important thing that you need to know is we can use else in the end, like the messages printed out when the
# loop ended for instance
b = 0
while b < 10:
    print("The value of b is: "+str(b))
    b = b + 1
    print("This line can be written some place else")
    print("*"*40)
else:
    print("Just broke out of the loop")
# So in above example the print statement under else was printed after the loop was finished
# There is one exception to that, if the loop is broken by a break statement that the else statement will not be
# printed
c = 0
while c < 10:
    print("This is the value of c: "+str(c))
    c = c + 1

    if c == 8:
        break
    print("This is nice")
    print('*'*40)
else:
    print("Just broke out of the loop")