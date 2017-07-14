"""
==  --> Equality Operator
!=  --> Not Equal to
<   --> Less Than
>   --> Greater Than
<=  --> Less Than or Equal to
>=  --> Greater Than or Equal to
"""

# Here, we are using the '==' which we are saying that 10 is equal to 10
# Notice, in the example first '=' is assigning the value to the variable and the
# second '==' is an operator which is comparator for the two values
bool_one = 10 ==10
print(bool_one)
# It will print True, to be honest I have no idea why it is printing 'True' but let's move and see if I can find out
print('*'*40)
# To understand better about why 'True' was printed let's assign another variable and instead of the same values let's
# give it different values
bool_two = 10 == 11
print(bool_two)
# So it says 'False' meaning in the variable we are saying that 10 is equal to 11 and the console is printing 'False'
# I think I'm understand the concept behind it
print('*'*40)

# Now we will use '!=' Operator, well basically it is the same thing as '=='
# Let's still work it
bool_three = 10 != 10
# We are saying 10 is not equal to 10 which is 'False' for if we print it the console will print 'False'
print(bool_three)
print('*'*40)
# And if we say '10 != 11' the console will print 'True'
bool_four = 10 != 11
print(bool_four)
print('*'*40)



# Same way with '<' Operator
bool_five = 10 < 10
print(bool_five)
print('*'*40)
bool_six = 9 < 10
print(bool_six)
print('*'*40)

# Same way with '>' Operator
bool_seven = 10 > 10
print(bool_seven)
print('*'*40)
bool_eight = 10 > 9
print(bool_eight)
print('*'*40)

# Same thing with '<=' Operator
bool_nine = 10 <= 10
print(bool_nine)
print('*'*40)
bool_ten = 9 <= 10
print(bool_ten)
print('*'*40)

# Same thing with '>=' Operator
bool_eleven = 10 >= 10
print(bool_eleven)
print('*'*40)
bool_twelve = 11 >= 10
print(bool_twelve)
print('*'*40)

# I think the instructor will show this in the next tutorial which is 'boolean_operators' but we can include some Mathematical Operations
# to our boolean for example
bool_thirteen = 10 >= 11 - 1
print(bool_thirteen)
# With above example we should get 'True' because 11 - 1 = 10 and 10 is equal to 10 and the boolean is true



















