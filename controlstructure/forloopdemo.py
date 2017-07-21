"""
Execute Statements repeatedly
Conditions are used to Stop the Execution of loops
Iterable items are String, List, Tuple, and Dictionary
"""

# This is the format of the for loop
# In the second line we
my_string = "Saad"
for c in my_string:
    print(c)
# This will print one letter in a line, but if you want to print the entire string in a line do like so
# 'c' is acting as a iterator, you can have anything there, it is just like a variable

my_nice_string = "Saad"
for nice in my_nice_string:
    print(nice, end=' ')
# By adding 'end=' you can print the entire variable in one line
print('*'*40)
print('*'*40)

# One of the use of the for loop is that we can replace the letter of the String
# Shown in the example below
my_very_string = "Saad"
for very in my_very_string:
    if very == 'a':
        print('A', end=' ')
    else:
        print(very, end=' ')
# The most important thing you need to remember is that you can pick any name for the iterator but make sure
# it is constant throughout
print()

cars_list = ["BMW", "Benz", "Honda"]
# So we have our list, now we can use the for loop to print out the names of car on the console
for car in cars_list:
    print(car)
# ******And also in the print() method use the iterator not the list name******

# So now if we want to create a list of numbers and do some mathematical operations with it we can do that
num_list = [1, 2, 3]
for n in num_list:
    print(n * 10)
# This is just taking an item from the list and multiplying it by 10
print('*'*40)

# So now we can do the same thing with the dictionary as well, let's define a dictionary and do some for loop
dic_1 = {'One': 1, 'Two': 2, 'Three': 3}
for key in dic_1:
    print(key)
print('*'*40)
# In dictionary by default the key will be printed, but if we want to print the value we can do that too
# Let's put the values next to the key and print it on the console
dic_2  = {'One': 1, 'Two': 2, 'Three': 3}
for keyvalue in dic_2:
    print("The key is: "+ keyvalue +" and the value for this key is: "+ str(dic_2[keyvalue]))
print('*'*40)

# There is another way of printing the key and value of the dictionary
for key, value in dic_2.items():
    print(key)
    print(value)
print('*'*40)