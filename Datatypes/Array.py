import array as arr
a = arr.array('i',[1,2,3])
print("Printing Array : ")
for i in range(0 , 3):
    print(a[i] , end=" ")

#insert()
a.insert(3,4)
print("\nPrinting array in after insert : ")
for i in (a):
    print(i,end=" ")
# access
print("\nAccess by index : ")
print(a[0])
# append
print("\nAppend Array : ")
a.append(5)
print(a)
# remove
print("\nRemove Element : ")
a.remove(5)
print(a)
# update 
print("Updating Array")
a[5] = 6
print(a)   