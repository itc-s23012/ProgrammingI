queue = []
queue.append(1)
print('queue:', queue)
queue.append(2)
print('queue:', queue)
print('pop from queue 1st value:', queue.pop(0))
print('pop from queue 2nd value:', queue.pop(0))
print('queue:', queue)

from queue import Queue

queue = Queue()
queue.put(1)
print('queue:', list(queue.queue))
queue.put(2)
print('queue:', list(queue.queue))
print('pop from queue 1st value:', queue.get())
print('pop from queue 2nd value:', queue.get())
print('queue:', list(queue.queue))

