# Basic operations in array

# importing array for array creations
import array as arr

# main array
arr = [1,2,3,4,5,6,7,8]

# Adding elements in array

print("Array before insetion: ", end="")
for i in range (0,8):
    print(arr[i],end=" ")
print()
print(arr)

# inserting array using insert() function
arr.insert(8,9)
arr.insert(9,10)

print("Array after insetion:",end=" ")
for i in (arr):
    print(i,end = " ")
print()
print(arr)

# Accessing elements in array


print("Access element at first index : ",arr[0])
print("Access element at second index : ",arr[1])

# deleting elements in array
# using pop() to remove element at any position
print("The array before popping:",arr)
print("The popped element is : ",end = " ")
print(arr.pop(4))
print("The array after popping:",arr)

print("Array after popping:",end=" ")
for i in range (0,9):
    print(arr[i],end=" ")
print("/r")

# it removes first occurence of 1
arr.remove(1)

print("Array after removing:",end = " ")
for i in range (0,8):
    print(arr[i],end=" ")
print()

# Searching element in array
# useing index() method for searching an element in array
print("The index of 1st occurence of 6 is: " ,end=" ")
print(arr.index(6))