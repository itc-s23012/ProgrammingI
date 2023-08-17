def square(x):
    if not isinstance(x, (int, float)):
        if isinstance(x, str) and x.isdigit():
            x = int(x)
        else:
            raise ValueError('square', x)
    return x ** x

print(square(2))
print(square('a'))

import sys
try:
    with open('test1.txt') as f:
        s = f.readline()
    print(s)
except FileNotFoundError:
    print('FileNotFoundError:', sys.exc_info())
except IOError:
    print('IOError:', sys.exc_info())
except ValueError:
    print('ValueError:', sys.exc_info())
except OSError as err:
    print('OSError:', sys.exc_info())
    print('err:', err)
except:
    print('Unexpected Error:', sys.exc_info())
