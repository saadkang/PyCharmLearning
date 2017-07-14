"""
Dictionary Methods
"""

car = {'Make' : 'Toyota', 'Model' : 'Camry', 'Year' : 2015}
cars = {'BMW': {'Model': '550i', 'Year': 2016}, 'Toyota': {'Model': 'Camry', 'Year': 2015}}
# key() is a built-in method that can help you get the key inside a dictionary
# values() is also a built-in method that can help you get the values of the key inside the dictionary
print(car.keys())
print(car.values())
# Now let's do the same thing with our cars dictionary as well
print('*'*40)
print(cars.keys())
print(cars.values())
print('*'*40)
# And if we want to see the key and the value at the same time we can use another method items()
# First we will try and print the keys and values set for car and then for cars
print(car.items())
print('*'*40)
print(cars.items())
# When you see the pair 'key:value' and this type of data is known as Tuple
print('*'*40)
print('*'*40)
# There is another method copy() that we can be used and that will copy the dictionary from one place to another
copy_car = car.copy()
print(car)
print(copy_car)
# There are a lot of different methods that we can use to do something with the dictionary
# Another method that was used in the tutorial is clear() that can be used to clear the data of the dictionary
copy_car.clear()
# So now the copy_car is cleared we will try it to print on the console
print('*'*40)
print(car)
print(copy_car)
# Now we will use the pop() method with the dictionary to remove a data from the car dictionary
# Let's first print the car as it is and then we will use pop() and then print after the pop() is applied
print('*'*40)
print(car)
print(car.pop('Model'))
print(car)
# Looking at the console I found out that pop() has a return type and that means that we can print the value of
# the key that was popped out

