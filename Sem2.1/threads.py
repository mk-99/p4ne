#!/usr/bin/python3

import threading
import time

global_count = 0

# Define a function for the thread
def print_time( threadName, delay):
    global global_count

    lock_global_count = threading.Lock()

    count = 0
    while True:
        time.sleep(delay)
        count += 1

        lock_global_count.acquire()
        try:
            global_count += 1
        finally:
            lock_global_count.release()

        print ("%s: count = %d, time is %s" % ( threadName, count, time.ctime(time.time()) ))

# Create two threads as follows
try:
    threading._start_new_thread(print_time, ("Thread-1", 1, ) )
    threading._start_new_thread(print_time, ("Thread-2", 2, ) )
except:
    print ("Error: unable to start thread")

while True:
    print(">>>> global_count = %d" % global_count)
    time.sleep(5)
    pass
