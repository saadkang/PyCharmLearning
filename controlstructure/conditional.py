"""
Conditional Logic
"""

# In Python instead of using the {} like in Java we use :
# So since there are no brackets Python completely rely on indentation
# This is how Python knows that if this condition is 'True' then do this otherwise do something else
if 100 > 10:
    print("Hundred is greater than 10")
print("It will always print")
# Now the above line is not indented so it is not associated with the if block meaning it will always be executed
print('*'*40)

# Now let's try it with variables instead of defining everything in the if block
value = 'green'
if value == 'green':
    print('Go')
else:
    print('Stop')
print('*'*40)
# We can change the value of the variable 'value' to red and the console will print 'Stop'
# Let's put 'else if' which is 'elif' in Python
# Meaning for traffic lights let's put all three conditions, let's also define a new variable to see different results
# So the value1 variable is 'red' and according to the conditions it should print 'Stop' the console
value1 = 'red'
if value1 == 'green':
    print('Go')
elif value1 == 'yellow':
    print('Prepare to Stop')
else:
    print('Stop')
print('*'*40)
# Now let's define a new variable and assign the value as 'yellow' and the console should print 'Prepare to Stop'
value2 = 'yellow'
if value2 == 'green':
    print('Go')
elif value2 == 'yellow':
    print('Prepare to Stop')
else:
    print('Stop')
print('*'*40)
# Now let's define a new variable and assign the value as 'green' and the console should print 'Go'
value3 = 'green'
if value3 == 'green':
    print('Go')
elif value3 == 'yellow':
    print('Prepare to Stop')
else:
    print('Stop')
print('*'*40)
# So that means we can have multiple 'if else' conditions and depending on the variable it will print out the results
# Also the most important thing to remenber is that the last condition says 'else' print that
# meaning if the value is 'green' print 'Go', elif value is 'yellow' print 'Prepare to Stop', and 'else' this
# this 'else' is saying whatever the value is other than green or yellow print 'Stop'
# To better understand that we are going to define a new variable and assign the value 'purple' and the console should
# print out 'Stop'
value4 = 'purple'
if value4 == 'green':
    print('Go')
elif value4 == 'yellow':
    print('Prepare to Stop')
else:
    print('Stop')
print('*'*40)
# See so the last condition is not associated with the value 'red' we can have any value other than 'green' or 'yellow'
# it will print 'Stop' on the console
# I was thinking do we have to use 'if' 'elif' 'else' what will happen if we use 'if' in all three places
# Let's try it
value5 = 'yellow'
if value5 == 'green':
    print('Go')
if value5 == 'yellow':
    print('Prepare to Stop')
if value5 == 'red':
    print('Stop')
print('*'*40)
# So I guess it is working and this way it is only concerned with these three value of the condition
# But I don't think that is the right way to right code
# I have asked him that question, let's see what he has to say in the matter, I will come back and write his
# response here