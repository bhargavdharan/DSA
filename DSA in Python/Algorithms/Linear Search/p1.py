# Linear search

# Given an array arr[] of n elements, write a function to search a given element x in arr[]
'''
A simple approach
1.start from leftmost element of arr[] and one by one compare x with each element of arr[]
2.if x matches with an element,return the index
3.if x doesn't match with any of elements,return -1

'''

def search(arr,n,x):

    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1

# Driver code
arr = [2,3,4,10,40]
x = 12
n = len(arr)

# Function call
result = search(arr,n,x)
if(result==-1):
    print("Element is not present in array")
else:
    print("Element is present in the array",result)