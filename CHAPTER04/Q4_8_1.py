def show_begin_end(func):
    def deco_func(*args, **kwargs):

        print('== start')
        result = func(*args, **kwargs)
        print('== end')
        return result
    return deco_func
import time
def sleep_for_a_while():
    print("Sleeping ..")
    time.sleep(2) # sleep for a while; interrupt me!
    print("Done Sleeping")

sleep_for_a_while()

@show_begin_end
def sleep_for_a_while():
    print("Sleeping ..")
    time.sleep(2) # sleep for a while
    print("Done Sleeping")
sleep_for_a_while()

import time

def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print('== start')
        result = func(*args, **kwargs)
        print('== end')
        return result
    return deco_func

def sleep_for_a_while():
    print("Sleeping ..")
    time.sleep(2) # sleep for a while
    print("Done Sleeping")

sleep_for_a_while()

@show_begin_end
def sleep_for_a_while():
    print("Sleeping ..")
    time.sleep(2) # sleep for a while
    print("Done Sleeping")

sleep_for_a_while()

