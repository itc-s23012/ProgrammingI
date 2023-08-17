def list_average(x):
    try:
        return sum(x)/len(x)
    except:
        print('list_length:', len(x))
        return None

print(list_average([3.9, 4.5, 2,3]))
print(list_average([]))

def list_average(x):
    return sum(x)/len(x) if len(x) > 0 else None

print(list_average([3.9, 4.5, 2, 3]))
print(list_average([]))

def to_int(x):
    try:
        return int(x)
    except:
        return None

print(to_int('a'))
print(to_int('5'))
