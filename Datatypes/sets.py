fruits = {"apple", "banana", "cherry"}


#add() The add() method adds an element to the se
# fruits.add("orange")
print(fruits)

#copy()	 	Returns a copy of the set
vegetables = fruits.copy()
print(vegetables)

#difference Return a set that contains the items that only exist in set x, and not in set y
fruits2 = {"google", "microsoft", "apple"}
diff = fruits.difference(fruits2)
print(diff)

# The difference_update() method removes the items that exist in both sets.
fruits -= fruits2 
print(fruits)