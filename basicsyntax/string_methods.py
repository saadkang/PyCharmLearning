# Accessing Characters in a String
state = "NC"[0]
print(state)

city = "Cary"
ct = city[2]
print(ct)

"""
len()   - Tells you the length of a variable
lower() - Changes all the characters in a variable to lower case
upper() - changes all the characters in a variable to upper case
str()   - Changes a variable to a String
"""

mix = "This is a Mixed Case"
print(mix.lower())
print(mix.upper())
print(len(mix))
print(mix + str(2))

"""
Concatenation
"""

print("Hello "+ " "+" World!!!")
print("We are getting the first letter of the variable state: " + state + " and then the variable city is: " + city)