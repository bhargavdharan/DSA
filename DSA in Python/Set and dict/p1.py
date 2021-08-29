# Built-in Data structures

'''
DICTIONARY - it is defined by key-value based separated by comma and enclosed in curly braces,key and value separated by colon
    syntax: {key:value,key1:value2..........}

    * keys must be immutable and values can be mutable
    * dict are unordered
    * we can access dict using key
    * dict are mutable


SET - it is collection of unique elements (so in set no item can repeated) and can't have duplicate values in the set
   syntax: {a,b,c,d..} and set("hello")
   * we can create set by using set constructor
   * duplicate values ignored in the set
   * set is unordered
   * set is mutable
   * set can take immutable objects as an element
   * it cannot be nested
   * we can access elements in sets by using (in membership) operator by loops
'''

# Dict
dict1 = {"name":"Ram","age":"21"}
print(type(dict1))
print(dict1)

d = dict()
print(type(d))
print(d)

dictionary1 = {"i":1,"j":2,"k":3,"l":4}
dictionary2 = {"i":1,"j":2,"k":3,"j":4}
print(dictionary1)
print(dictionary1["i"])
print(dictionary1["j"])
print(dictionary1["k"])
print(dictionary2)
print(dictionary2["i"])
del dictionary2["j"]
print(dictionary2)

print(dictionary1 == dictionary2)

# set

st = set("Hello")
print(type(st))
print(st)

s = set([1,2,3,4])
print(type(s))
print(s)
a = 1 in s
print(a)


set1 = {1,2,3,4}
print(set1)

print( s == set1 )

set1.add(5)
print(set1)

