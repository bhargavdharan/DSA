# implementing stack using modules
# collections - deque(double ended queue)
# Queue - lifoqueue(push-->put, pop-->get)

import collections


stack = collections.deque()
print(stack)

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

stack.pop()
stack.pop()
stack.pop()
print(stack)

a = not stack
print("is stack stack is empty?",a)
