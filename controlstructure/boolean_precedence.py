"""
1. not
2. and
3. or
"""


# Ok, so the precedence of 'not' 'and' 'or' is respectively also shown above in green
bool_output = True or not False and False
# Let's work the above boolean: not False is 'True', True and False is 'False', and True or False is 'True'
# So, if we print this the console should print 'True'
print(bool_output)


# Now, let's put the above example in words with same conditions and everything
bool_output0 = 10 == 10 or not 10 > 10 and 10 > 10
# We can write this is brackets to make our code clean
bool_output1 = (10 == 10) or not (10 > 10) and (10 > 10)
print(bool_output1)
print('*'*40)

# The brackets also helps us change the order of precedence of the conditions
# If you put the brackets around the numbers like in the example above you didn't really change the order
# But if you include some other things in the brackets you changed the order, shown in example below
bool_output2 = (10 == 10 or not 10 > 10) and 10 > 10
# In above example we are telling it to work on the conditions that are inside the brackets and then move on to
# the outside of the brackets. Which changed the result on the console from 'True' to 'False'
print(bool_output2)