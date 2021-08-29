def search(arr,x):
    for index, value in enumerate(arr):
        if value == x:
            return index
    return -1

arr = [1,10,30,15]
x = 30 
print(x,"is present at index",search(arr,x))
