x = list(range(1, 6))
print(x)
del x[-2:]
print(x)

print([i for i in range(5)])

import gc
b = [x for x in range(100000)]
del b
print(gc.collect())

import sys
print(sys.getsizeof([x for x in range(10)]))
