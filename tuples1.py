# Tuples
#immutable
#ordered
#allows suplicates
tupl1 = (1,2,3,4,5)
print(tupl1) #(1, 2, 3, 4, 5)

#len()
print(len(tupl1)) #5

#Negative Indexing
print(tupl1[-3]) #3

#count()
print(tupl1.count(5)) #1

#Slicing
print(tupl1[::-1]) #(5, 4, 3, 2, 1)

#copy()
tupl2 = tupl1
print(tupl2) #(1, 2, 3, 4, 5)

#index()
print(tupl1.index(2)) #1

#clear()
#tupl1.clear() #AttributeError: 'tuple' object has no attribute 'clear'
#tupl1.clear()
#print(tupl1) #()

