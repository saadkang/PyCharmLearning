"""
Variable Scope
"""

a = 10

def test_method(a):
    print("The value of local 'a' is: " + str(a))
    a = 2
    print("The new value of local 'a' is: " + str(a))

print("The value of global 'a' is: " + str(a))
test_method(a)
print("Did the value of global 'a' changed? " + str(a))
print("*" * 40)
# In the example above when we used the same variable name, even if we have the same variable name but since we didn't
# change it the global variable is not changed


# Now, we will use the same, example but in up coming example we will change the global variable
b = 20

def test_method1():
    global b
    print("The value of 'b' inside the method is: " + str(b))
    b = 2
    print("The value of new 'b' inside the method is changed: " + str(b))

print("The value of global 'b' is: " + str(b))
test_method1()
print("Did the value of global 'b' changed? " + str(b))
print("*" * 40)