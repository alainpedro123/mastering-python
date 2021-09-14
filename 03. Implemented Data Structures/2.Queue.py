# 14. QUEUES
# First In First Out

from collections import deque

# it allow us to dequeue and shift all the elements to the left/right
queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

# checking if the queue is empty
if not queue:  # that means we have an empty stack
    print("empty")
    # do something
