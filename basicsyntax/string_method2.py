# Now we are going to replace the value of a variable

# So replace method has 3 parameters(old, new, count)
# count is asking you at how many places you want to replace it
# If you only have one old entry then don't worry about the count but if you have same entry multiple time mention it

nameOfFruits = "Bananas, Oranges, Apples, Bananas"
print(nameOfFruits.replace("Bananas", "Mangoes", 1))
print("********************")

# sub-String
# Starting index is inclusive
# Ending index is exclusive
subOfnameOfFruits = nameOfFruits[0:7]
print(subOfnameOfFruits)

# You can skip index when you are printing them
skipNameOfFruits = nameOfFruits[0:7:2]
print(skipNameOfFruits)
print("So in above example we are still printing String index 0 to 6 but the second : is telling you to skip,\
 so to better understand this all the capital letters are skipped 'bAnAnAs'")