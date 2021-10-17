'''
Exercise 3a – A queue to the rescue
Background
Whenever there’s a “first in, first out” thing going on, queues tend to be useful as a data structure. 
For example, a game may use a queue to process the players’ actions in order, a supercomputer may use 
a queue to execute tasks in the order that they arrive, and a logging tool may use a queue to store 
log messages for a while before writing them to a file.

Let’s demonstrate how a queue can help us. Here is a function fifo_list that creates a list and then 
empties it by repeatedly removing its first element. We can measure the time it takes to execute:
'''
from timeit import timeit
from collections import deque


def measure(function):
    time = timeit(function, number=TIMES)
    time_str = f"Execution time: {time/TIMES:.7f} seconds"
    settings = f"(SIZE: {SIZE}, TIMES: {TIMES}, {function.__name__})"
    print(time_str, settings)


def fifo_list():
    a_list = list(range(SIZE))
    while a_list:
        a_list.pop(0)


def deque_test():
    # skapa en FIFO kö
    a_queue = deque(range(SIZE))
    while a_queue:
        a_queue.popleft()


SIZE = 100000
TIMES = 10
print()
measure(fifo_list)
measure(deque_test)
print()

'''
Tasks
1. Define a function fifo_deque which creates a deque:
a_queue = deque(range(SIZE))
and empties it:
a_queue.popleft()
It should be similar to fifo_list above
2. Compare the execution times and try different sizes of the queue and list. 
You will notice that one is significantly faster when SIZE is big. Why is this?
'''
