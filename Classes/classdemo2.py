"""
Object Oriented Programming
"""

# Class is a blueprint or the template that defines the object

class Car(object):
    def __init__(self, make):
        self.make_car = make

# To create the instance of the class just type the following
# c1 = Car()  <--- I have to comment this out because without that the program is not going to run
# We can not run the program this way because, the class 'Car()' has a parameter, so we have to include that in there
# and we don't have to include the 'self' parameter because that is by default meaning we have to include the parameter
# 'make_car'
# Basically it is the same thing without the keyword 'new', you know in Java we would write 'Car() c1 = new Car()'
c1 = Car('bmw')
# ************c1 is not the instance, it the reference variable************
print(c1.make_car)
