## queue implement uig deueue collection
import collections

queue = collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)

print("Initial queue:", queue)
queue.pop()
print("Queue after dequeue:", queue)

## using queue module

import queue
q = queue.Queue(maxsize=10)
for _ in range(5):
    q.put(_)

print(f"Queue size after enqueuing 5 elements: {q}")

el = q.get
print(f"Dequeued element: {el}")

