"""
Execute Statements repeatedly
Conditions are used to Stop the Execution of loops
Iterable items are String, List, Tuple, and Dictionary
"""

x = 0
while x < 10:
    print("The value of x is: "+ str(x))
    x = x + 1
print('*'*40)
print('*'*40)
# So like established before after the while block whatever is indented is part of the while block
# In the above example we defined x is 0, and then we are basically saying that as long as x is less than 10
# print 'The value of x is:' 'whatever the value of x is' and in the next line we are increasing the value of x
# by one and continuing with the loop as long as the value of x is less than 10, once the value of x exceeds 10
# the loop will break or stop


# We can use the while loop to put the value in a list
l = []
num = 0
while num < 10:
    l.append(num)
    num += 1
print(l)
print('*'*40)
# So we have an empty list 'l' and we defined a variable 'num' that holds the number or value '0'
# and in the while loop we are saying as long as 'num' is less than 10 do what it says in the loop, and the loop is
# saying to append() meaning add the value of 'num' in the list and in the next line we are increasing the value of
# the variable 'num' by 1 and then the loop continues until the value of the variable reaches 9. After the vaule of
# the variable 'num' reaches 10 the condition of the while loop is not met and the loop breaks, the last line is not
# part of the while block so it get executed anyways and it is saying to print the list 'l' and the list is printed
# on the console



# We can add another line in the while loop asking to print the value of a variable
j = []
num2 = 0
while num2 < 10:
    j.append(num2)
    print("The value of num is: "+ str(num2))
    num2 += 1
print(j)