"""
Data type to store more than one value in one variable name, in terms of key value pair
Dictionary items are in brackets {} in {key:value} pair, separated by "," {'k1':'v1', 'k2':'v2'}
Dictionary is not sequenced and no specific index --> Mapping, so basically there is no order
"""

cars = {'Make' : 'Toyota', 'Model' : 'Camry', 'Year' : 2015}
print(cars)
print(cars['Make'])
print(cars['Model'])
print(cars['Year'])
print("*"*40)
# We can store the value in the variable and then print it
make = cars['Make']
print(make)
print("*"*40)
# We can define an empty dictionary
emptyDictionary = {}
# Now we can print that empty dictionary on the console: it is just be {}
print(emptyDictionary)
print("*"*40)
# Adding items to the dictionary
# We can use the same empty dictionary that we have already defined
emptyDictionary['One'] = 1
# Now let's print it and see what gets printed
print(emptyDictionary)
print("*"*40)
# We can add more items to the dictionary
emptyDictionary['Two'] = 2
emptyDictionary['Three'] = 3
# Now let's print it again
print(emptyDictionary)
print("*"*40)
# Now that the items are added we can do more operations with it
# Let's define a variable and do a addition with to the second dictionary we created
adding = emptyDictionary['Two'] + 8
print(adding)
print("*"*40)
# Now we will change the entries of the dictionary as well, let's use the 'emptyDictionary' for example
print(emptyDictionary)
emptyDictionary['Two'] = 10
print(emptyDictionary)