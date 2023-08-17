mountain_in_japan = {'fuji': 3776, 'kitadake': 3193, 'okuhodakadake':
  3190, 'dummy': 0}

mountain_in_japan = {'fuji': 3776, 'kitadake': 3193,
                     'okuhodakadake': 3190, 'dummy': 0}
mountain_in_japan_sorted = sorted(mountain_in_japan.items(),
                                 key=lambda x: x[1], reverse=True)
print(mountain_in_japan_sorted)

mountains = {'fuji': 3776, 'kitadake': 3193, 'okuhodakadake': 3190, 'dummy': 0}
sorted_mountains = sorted(mountains.items(), key=lambda x: x[1], reverse=True)
print(sorted_mountains)

intdict = {'1': 'one', '2': 'two', '3': 'three'}
for key, val in intdict.items():
    print(key, val)

a = ['fuji', 'kitadake', 'okuhodakadake']
for i, mt in enumerate(a):
    print(i, mt)
