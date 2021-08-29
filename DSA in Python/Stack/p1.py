# user defined data structures

'''
stacks -- 
         * it is the ordered collection of items
         * addition of items and removal of items can be done on same end
         * we can simply memorize stack as FIFO(fist in first out) or LIFO(last in first out)
    Basic operations performed by stack
        1.push        --- it adds elements to the stack
        2.pop         --- it removes elements from the stack
        3.peek or top --- it shows which element present at the top
        4.isEmpty     --- it tell you whether stack is empty or not

  Application of stack:
    * stacks are considered as backbone of data structures
    * we can use stack to reverse the string
    * we can use in expression evaluation and expression convertion
    * it is used in algorithms such as tower of hanoi

   different ways to implement stack:
   1.by using lists (push-->append,pop-->pop)
   2.by using modules
'''

# implementation of stack

stack = []
# append function to push
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
a = (len(stack) == 0)
print(stack)
print(a)

# Accessing elements from stack
print("Accessing elements.....")
print("first element in the stack:",stack[1])
print("last element in the stack:",stack[-1])

# pop() function to pop
# element from stack in
# LIFO order
print("\n Elements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\n stack after elements are popped:")
print(stack)
a = (len(stack) == 0)
print(a)
print(not stack)