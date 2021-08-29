#implementation of queue using modules
# Method-1 : collections - deque

import collections

q = collections.deque()
print(q)

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)

q.pop()
print(q)
q.pop()
print(q)
q.pop()
print(q)
# q.pop()
# print(q)
a = not q
print(a)

q.append(10)
q.append(20)
q.append(30)
q.append(40)
print(q)

q.popleft()
print(q)
q.popleft()
q.popleft()
q.popleft()
print(q)
a = not q
print(a)

q.append(10)
q.append(15)
q.append(20)
q.append(25)
print(q)
print("last element in queue:",q[-1])
print("first element in the queue",q[0])


