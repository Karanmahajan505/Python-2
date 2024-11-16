students = ("Atharv","Alfaj","Piyush",1,1,2,1,1,1,1)
# Methods in tuples 

#index() Searches the tuple for a specified value and returns the position of where it was found
print("Index of piyush : " , students.index("Piyush"))

#count() 	Returns the number of times a specified value occurs in a tuple
print("\nhow many times a '1' occurs : ",students.count(1))

#join() To join two or more tuples
fruits = ("Banana" , "Mango" , "Apple")
tuple3 = students+fruits
print(tuple3)

