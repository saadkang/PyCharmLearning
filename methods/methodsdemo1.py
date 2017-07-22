# In the past when we have to get the sum of numbers we would just put them in a variable and print it
# But we can use a method to do the same so that way we don't have to re-write it

def addition():
    print(3 + 2)
addition()
print('*'*40)
# So whenever we are defining a method we have to use 'def', and in method we are printing the sum of 3 and 2 but
# it will not print anything unless we call that method and the third line is how you call the method.


# The same thing java, we can define the parameters of the methods
def subst(n1, n2):
    print(n1 + n2)
subst(3, 3)
subst(2, 8)
print('*'*40)


# For the educational purposes we will be talking about the list, that how can you add item to the list and maybe
# print out the length of the list on the console
demo_list = [1, 2, 3]
print(demo_list)
print(demo_list.append(4))
print(demo_list)
print(len(demo_list))