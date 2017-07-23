"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""

# So with the positional parameters we are assigning the default values to the variable
def sum_num(n1 = 2, n2 = 4):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

# So, when we have given the default values to the variables, if we don't assign the new values to the variables
# then the default values will be used.
sum1 = sum_num()
print("In here we didn't assign new values so it is using the default one and the sum is: %s" % sum1)
print("*"*80)
# In the example below, we are assigning the different values to the parameters, so it will do the calculations with
# the new assigned values
sum2 = sum_num(2, 8)
print("In here we are assigning new values so it will not be using the default one and the sum is: %s" % sum2)
print("*"*80)


# There is one other thing we can do with the parameters
sum3 = sum_num(n2 = 2, n1 = 1)
print(sum3)
# So with the example above, we have used 'n1' and 'n2', so that way the position doesn't matter
# Also, we can only assign one value, for instance we can say 'n2 = 5' and don't assign the value for 'n1'
# so 5 will be assigned to n2 and since we didn't assign any value to n1 it is going to be the default value