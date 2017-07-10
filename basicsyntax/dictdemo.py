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
# Adding 