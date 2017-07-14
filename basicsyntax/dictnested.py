"""
Nested Dictionary:
d = {'k1' : {'nestk1' : 'nestvalue1', 'nestk2' : 'nestvalue2'}}
"""

cars = {'BMW': {'Model': '550i', 'Year': 2016}, 'Toyota': {'Model': 'Camry', 'Year': 2015}}
Toyota_Year = cars['Toyota']['Year']
print(Toyota_Year)
print('*'*40)
# You can print stuff from nested dictionary by creating another variable but if you want
# you don't have to create a variable you can just type everything in the print statement
print(cars['BMW']['Model'])
# And the most important thing to know is that the nested thingy don't stop at two you can
# go as nested as you want, for instance you can have a nested dictionary inside a nested
# dictionary