"""
Now we are going to talk about list in detail, manipulation of it
"""

cars = ["Toyota", "Honda", "Audi"]
length = len(cars)
# When you are using the method len() in python it will return the number of items in that list
print("The number of items in the list cars is: %s" % length)
print(cars)
# append method will add the value at the end of the list
cars.append("Benz")
print(cars)
# What if we don't want to add the value at the end of the list but we want to add at a specific location
cars.insert(1, "Jeep")
print(cars)

# Now, let's say we want to find the index of a specific value, for instance 'Audi'
# We can create a new variable and use a index method in that one to find the index number
indexOfAudi = cars.index("Audi")
print("The index of Audi is: %s" % indexOfAudi)

# Now we will be working on removing the item from the list
# There are two different methods that we can use, pop and remove
removeItemByPop = cars.pop()
# I think the pop removes the last item on the list
print(removeItemByPop)
# By using the above code line, we can see what was removed from the list
print(cars)
removeAgainByPop = cars.pop()
print(removeAgainByPop)
print(cars)
# This confirms it that the pop method removes the last item on the list

# Now we know that the pop method removes the last item on the list
# What if we don't want to remove the last item on the list but we want to remove a specific item from the list
# To do that we can use the method remove and specify the item name
print("*"*40)
print(cars)
# The remove method don't have a return type, but pop method does
cars.remove("Jeep")
print(cars)
print("*"*40)
# Now, let's talk about skipping and slicing a list and we what we can do with it
cars.append("Audi")
print("The original list cars is: %s" % cars)
skip = cars[0:2]
print(skip)
print("*"*40)
# So, skipping and slicing is the same thing as before, you can print one or more index of a list or you can print the entire list
# Like so..we don't have to define a variable and then print the needed item from the list we can just do it like below..
print(cars[:])
print("*"*40)
# We can only print on item from the list, let's say we want to print item on the 0 index only
print(cars)
print(cars[0:1])
print("*"*40)
# Also now we want to print everything except the index 0
print(cars)
print(cars[1:])
# You can do it the way you did above, which is a better option, but if you want to do it in way you did below you
# can do it but it is not recommended
print(cars[1:len(cars)])
print("*"*40)
# Now, if we want to print the item on the last index and we don't know how many items are in the list
print(cars)
print("If you do it this way you will not see the item inside the quotations: "+cars[-1])
print("If you do it this way you will see the item inside the quotations: %s"% cars[-1:])
print("*"*40)
# Now, let's do the sorting of the list
print(cars)
cars.sort()
print(cars)