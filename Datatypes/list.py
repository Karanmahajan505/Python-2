students = ["Atharv","Alfaj","Piyush"]
print(students)

#The append() method appends an element to the end of the list.
print("\nAppend : ")
students.append("Kunal");
print(students)

# clear() Removes all the elements from the list
print("\nClear : ")
students.clear()
print(students)

#copy() Returns a copy of the list
print("\nCopy : ")
seniors = students.copy()
print(seniors)

#count() Returns the number of elements with the specified value
print("\nCount : ")
no = students.count("Kunal")
print("NO students : " , no)

#extend() Add the elements of a list (or any iterable), to the end of the current list
print("\nextend : ")
roll=[1,2,3,4]
students.extend(roll)
print(students)

#index() Returns the index of the first element with the specified value
print("\nindex : ")
print("Kunal's index : " , students.index("Kunal"))

# insert()	Adds an element at the specified position
print("\ninsert : ")
students.insert(1,"Harsh")
print(students)

#pop() Removes the element at the specified position
print("\npop : ")
students.pop(1)
print(students)

#remove()	Removes the first item with the specified value
print("\nremove : ")
students.remove("Kunal")
print(students)

#reverse()	Reverses the order of the list
print("\nreverse : ")
students.reverse()
print(students)

#sort() sort resource
print("sort :  ")
sorting = ["Atharv","Alfaj","Piyush"]
sorting.sort()
print(sorting)