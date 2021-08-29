# built-in data structures
'''
 LIST --- it is the collection of the zero and many elements separated by comma and enclosed in square brackets
           ex :[1,2,3,4,5]
* They are two ways to implement list by enclosed elements in square brackets and anotherway to create list is u can use the list constructor
* list can store data of different data types
* lists are ordered
* we can access list elements using indexing
* we can use positive and negative indexing
* lists can be nested
* lists are mutable
* lists are dynamic

 TUPLEs --- it is also collection of the zero and many elements separated by comma and enclosed in parenthesis
            ex:(1,2,3,4)
* tuples are immutable
* it stores the data of different types
* it is also nested
* it is also use positive and negative indexing

conclusion :
* why we need tuple instead of list?
* --- tuple is faster than the list and sometimes u don't want data to be modified
* --- if the values of the program remains constant for the life of the program using tuple instead of list guards against the accidental modification



'''

# Lists
list1 = [1,2,3,4,5]
print(type(list1))
print(list1)

print(list1[0])
print(list1[1])
print(list1[2])

print(list1[-1])
print(list1[-2])
print(list1[-3])

list2 = [1,3,4,5,6]
print(list2)
list2.append(7)
print(list2)

list3 = [(1,2),1,2,3]
print(list3)

# Tuples

tuple1 = (1,2,3,4,5)
print(type(tuple1))
tuple2 = (6,7,8,9,10)
print(tuple2)

