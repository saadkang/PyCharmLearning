"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""

# The above thing is called 'dock string' this is the description of the file that we are working on.

# It is continuous from the first demo, the instructor wrote the same methods here, but I'm not going to
# because it is waste of time
def multi_num(n1, n2):
    print(n1 * n2)
# This above code is not going to print anything on the console because we are not calling the method


# Let's talk about 'dock string' in the next example, in any kind of coding, it is a good habit to write the
# description of the code, meaning write down what you are doing or trying to accomplish in the code, so that
# if someone else is looking at the code and they can't understand they will know from the 'comments' or 'dock string'
# After defining the method, we can write the three double quotes like always but this time the Python we auto-write
# the parameters and the return if the method is a return type method
def subs_num(n1, n2):
    """
    This method is going to subtract two variables and can be used upon calling it
    :param n1:
    :param n2:
    :return:
    """
# And instead of writing "print(n1 - n2)" in the next line after we have define the method we can write
    return n1 - n2
subs_num(8, 4)
subs_num(9, 1)
# What this above statements are going to do is do all the calculations with the integers and will still
# not going to print anything on the console because we have not called the method

# Now, what we can do is save the return value in a variable and then we can print that variable
subs1 = subs_num(8, 4)
subs2 = subs_num(9, 1)

# Now, that we have saved the values in the variables 'subs1' and 'subs2', if we want we can print those variables
print(subs1)
print(subs2)
print("*"*40)
# And the console print-out the difference of the two integers that was saved in the variables


# Let's talk about another example to better understand the 'return' keyword in Python
# In Java I used 'Camel Casing' so I think I will stick with that
def isNorthCarolina(city):
    cityList = ["Cary", "Raleigh", "Holly Springs", "Dunn"]

    if city in cityList:
        return True
    else:
        return False
cities = isNorthCarolina("Cary")
print(cities)
print("*"*40)


# One of the student of this class, pointed out that you don't have to use the 'if/else' to get the same result
# one can get type 'return city in cityList' and will get the same result, so let's try it and see for ourselves
def isNewYork(city):
    cityList1 = ["New York City", "Pomona", "Nunuet", "Rockleigh", "Manhattan"]
    return city in cityList1
cities1 = isNewYork("Manhattan")
print(cities1)
print("*"*40)
# So yea we don't have to use 'if/else' to get the same answers