# User defined Data structures
'''
Queue:
    * Queue is the linear data structure,where the element is inserted on the oneside and removed on other side.
    * Queue is open on both ends i.e insertion and deletion can be occur on both ends.
    * where the element is added is called back/rear/tail
    * where the element is deleted is called front/head.
    * it follows FIFO and LIFO principle
    * the process adding elements in queue is called enqueue and the process of removing elements is called dequeue.
#Operations performed in Queue
 1.enqueue
 2.dequeue
 3.isFull
 4.isEmpty

**where we can use queue?
---> queues are used whenever used to process things one at a time.
 ex: Applying bunch of photos,printing multiple documents

** how to implement Queue?
---- we can implement queues in two ways 1. lists 2. modules


'''

# Implementation of Queue.
# enqueue----append method
# dequeue----pop method

queue = []
queue.append(10)
print(queue)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
print(queue)

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

queue.insert(0,10)
queue.insert(0,20)
queue.insert(0,30)
print(queue)

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

a = not queue
print(a)

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

a = not queue
print(a)

