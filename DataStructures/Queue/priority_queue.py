## Priority queue implementation using heap queue module
import queue
q = queue.PriorityQueue()
q.put(10)
q.put(30)
q.put(20)
q.put(-10)
q.put(30)

print("Initial priority queue:", list(q.queue))
el = q.get()
print("Dequeued element:", el)

# queue = []
# queue.append(10)
# queue.append(30)
# queue.append(40)
# queue.append(20)

# print("Initial queue:", queue)
# queue.sort()
# print("sort queue", queue)

# el = queue.pop(0)
# print("Dequeued element:", el)

