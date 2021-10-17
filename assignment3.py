from typing import Any, Counter
from timeit import timeit

'''
Tasks
Your task is to modify an implementation of a doubly ended queue SimpleQueue that will enable handling 
updates in a FIFO manner. Two operations remain to be implemented: append and popleft. 
You can find the unfinished implementation of SimpleQueue in simplequeue.py also attached in this assignment.

When you have implemented append and popleft, you must remove all the other methods(except the constructor) 
to save memory. You then need to measure its execution time for 1'000'000 messages, to ensure that it 
performs well enough. You can use the code from Exercise 3a to do this, then submit by including the results 
of your measurement together with a link to your GitHub repository. You may need to remove the measuring of 
fifo_list since it is so slow.

Acceptance criteria
• Your boss is happy
• Your GitHub repository contains a week3 folder with the finished implementation of SimpleQueue in a file 
  simplequeue.py, along with the code that you used to measure its execution time in a separate file measure.py
• simplequeue.py contains only your SimpleQueue implementation with a constructor and no other methods than 
  append and popleft
• measure.py contains the code you used for measuring the queue’s performance(the parts that won’t be sent to 
  the rocket heading for Venus)
• You have submitted the results of your measurement and a link to your GitHub repository here in itslearning

'''


class Node:
    # A node of a doubly linked list has a value and two node references
    # value kan vara av vilken typ som helst "Any" & konstruktorn returnerar inget "None"
    # Se Any som en class, typ av objekt
    # obs att direction är till vänster!  Next node <-Next/Value/Prev-> Prev node
    def __init__(self, value: Any) -> None:
        self.value: Any = value  # betyder att value kan vara vad som helst
        self.prev: Node = None   # betyder att prev pekar på inget/None av typen "Node"
        self.next: Node = None   # efter : kommer en hint/tips


# detta är en kö av noder med en head och en tail
class SimpleQueue:
    # A doubly linked list
    # <-Next/Value/Prev->
    def __init__(self) -> None:
        self._head: Node = None
        self._tail: Node = None

    def append(self, value: Any) -> None:
        # Adds node with specified value at end of queue
        # Assignment 3: Implement this method
        new_node = Node(value)
        if self._head:                  # körs endast om det finns en _head!
            new_node.next = self._tail  # ny nod next pekar på gamla tail
            new_node.prev = None        # finns inget till höger!

            # replaces references in previous tail, note still same next reference
            self._tail.prev = new_node
            self._tail.next = self._tail.next  # dvs ändras inte!

            # Update tail to the new_node
            self._tail = new_node

        else:
            # denna körs bara första gången om self._head saknas!
            # nya noden blir både head & tail
            self._head = new_node
            self._tail = new_node

    def popleft(self) -> Any:
        # Assignment 3: Implement this method
        # Removes node at beginning of queue and returns its value
        value = self._head.value         # värdet på head, första noden
        self._head = self._head.prev     # ta ett steg till höger -- prev
        try:
            self._head.next = None
        except AttributeError:
            self._head = None
        return value


def PrintQueue(my_queue: SimpleQueue):
    if my_queue._head:
        current_node = my_queue._head
        print("Head =", my_queue._head.value)
    else:
        print("Head = None")
    while current_node.prev != None:
        current_node = current_node.prev    # ett steg till höger
        if current_node.prev != None:
            print("Body =", current_node.value)
        else:
            print("Tail =", current_node.value)

    # current_node = my_queue._head
    # while current_node.prev != None:    # loopa tills det inte finns något mer till höger
    #     print(f"This is the value of our node: {current_node.value}")
    #     current_node = current_node.prev
    # # skriv ut ista raden också!
    # print(f"This is the value of our node: {current_node.value}")


def measure(function):
    time = timeit(function, number=TIMES)
    time_str = f"Execution time: {time/TIMES:.7f} seconds"
    settings = f"TIMES: {TIMES}, {function.__name__})"
    print(time_str, settings)


def send_messages():
    queue = SimpleQueue()
    for x in range(TIMES):
        queue.append('The')
        queue.append('Trouth')
        queue.append('Is')
        queue.append('Out')
        queue.append('There')


TIMES = 500   # TIMES = antal gånger x 5, dvs 100x = 20


def main():

    time = timeit(send_messages, number=TIMES)
    print(f"Execution time: {time/TIMES:.7f} seconds")
    print(f"Number of messages sent: {TIMES*5}\n")


if __name__ == "__main__":
    main()
