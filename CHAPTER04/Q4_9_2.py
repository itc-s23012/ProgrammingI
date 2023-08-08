import os, sys
MAX = 2
print(sys.getdefaultencoding ())
print(os.path.basename(os.getcwd ()))
for i in range( 3 ) :
    print(i , end=" ")
    if MAX>i:
        print(MAX)
    else :
        print ("#")

import os
import sys
MAX = 2
print(sys.getdefaultencoding())
print(os.path.basename(os.getcwd()))
for i in range(3):
    if MAX > i:
        print(MAX)
    else:
        print("#")

import os
import sys

MAX = 2
print(sys.getdefaultencoding())
print(os.path.basename(os.getcwd()))

for i in range(min(MAX+1, 3)):
    print(MAX if MAX > i else "#")

