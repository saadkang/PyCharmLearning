"""
and
******************************
True and True    --> True
False and True   --> False
True and False   --> False
False and False  --> False

or
******************************
True or True    --> True
True or False   --> True
False or True   --> True
False or False  --> False

not
******************************
not True         --> False
not False        --> True
"""

# Now let's work all of this in a code and see if it is correct
# First let's work the 'and'
# Both conditions are 'True' so it should print 'True' in the console
and_output1 = (10 == 10) and (10 > 9)
print(and_output1)
# First condition is 'True' and the second condition is 'False' so the console should print 'False'
and_output2 = (10 == 10) and (10 < 9)
print(and_output2)
# First condition is 'False' and the second condition is 'True' so the console should print 'False'
and_output3 = (11 == 10) and (10 > 9)
print(and_output3)
# Both conditions are 'False' so the console should print 'False
and_output4 = (11 == 10) and (10 < 9)
print(and_output4)
# That proof the 'and' conditions
print('*'*40)


# Now let's work all of the conditions for 'or'
# Both conditions are 'True' so the console should print 'True'
or_output1 = (10 == 10) or (10 > 9)
print(or_output1)
# First condition is 'True' and the second condition is 'False' so the console should print 'True'
or_output2 = (10 == 10) or (10 < 9)
print(or_output2)
# First condition is 'False' and the second condition is 'True' so the console should print 'True'
or_output3 = (11 == 10) or (10 > 9)
print(or_output3)
# Both conditions are 'False' so the console should print 'False'
or_output4 = (11 == 10 ) or (10 < 9)
print(or_output4)
# That proof the 'or' conditions
print('*'*40)

# Now let's work all of the conditions for 'not'
# First let's work with 'not' 'True'
# Meaning we are going to say something 'True' but put 'not' in front of it and console should print 'False'
not_output1 = not (10 == 10)
print(not_output1)
# Let's also see what happens when we remove the 'not' from the above example and when we print it, it should print 'True'
not_output2 = (10 == 10)
print(not_output2)
# Now let's see the same workout process with 'not' 'False', on the console we should see 'True'
not_output3 = not (11 == 10)
print(not_output3)
# Let's alse see what happens when we remove the 'not' from the abouve example and when we print it, it should print 'False'
not_output4 = (11 == 10)
print(not_output4)