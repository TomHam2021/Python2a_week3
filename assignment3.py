from typing import Any, Counter

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

    def appendleft(self, value: Any) -> None:
        # Adds node with specified value at beginning of queue
        new_node = Node(value)
        try:                             # Assume queue is not empty
            # sätter self._head till new_node.prev(den nya noden)
            new_node.prev = self._head
            self._head.next = new_node
            self._tail = self._tail      # dvs ändras inte!
        except AttributeError:           # Queue is empty
            self._tail = new_node        # dvs new node blir både head & ..
        self._head = new_node            # .. tail

    def pop(self) -> Any:
        # Removes node at end of queue and returns its value
        value = self._tail.value         # värdet på sista noden
        self._tail = self._tail.next     # ta ett steg till vänster = framåt
        # om man redan står på _head är self._tail.next = None
        try:                             # Delete reference to removed node
            self._tail.prev = None       # detta går inte om ..
        except AttributeError:           # Queue became empty
            self._head = None
        return value

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

    def add(self, index: int, value: Any) -> None:
        """Inserts a node with specified value at index"""
        new_node = Node(value)
        if self._head:                   # Queue is not empty
            node = self._head
            for _ in range(index):
                node = node.prev
            if node:                     # Inserting in middle or at beginning
                if node.next:            # Inserting in middle of queue
                    node.next.prev = new_node
                    new_node.next = node.next
                else:                    # Inserting at beginning of queue
                    self._head = new_node
                new_node.prev = node
                node.next = new_node
            else:                        # Inserting at end of queue
                new_node.next = self._tail
                self._tail.prev = new_node
                self._tail = new_node
        else:                            # Queue is empty
            self._head = new_node
            self._tail = new_node

    def remove(self, index: int) -> None:
        """Removes node at specified index"""
        node = self._head
        for _ in range(index):           # Find the node with specified index
            node = node.prev
        if node.prev:                    # Removing from middle or at beginning
            node.prev.next = node.next
        if node.next:                    # Removing from middle or end of queue
            node.next.prev = node.prev
        if node == self._head:           # Removing from beginning of queue
            self._head = node.prev
        if node == self._tail:           # Removing from end of queue
            self._tail = node.next

    def to_list(self):
        """Returns a list with the queue node values"""
        values = []
        node = self._head
        while node:                      # Iterate from head to tail
            values.append(node.value)
            node = node.prev
        return values

    def __str__(self):
        """Returns a string representation of the queue"""
        values = ", ".join(self.to_list())
        return f"SimpleQueue([{values}])"


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


def main():

    my_queue = SimpleQueue()
    my_queue.append(0)  # number value is not relevant
    my_queue.append(1)
    my_queue.append(2)
    my_queue.append(3)
    print("Entering loop that goes from head -> tail")
    PrintQueue(my_queue)
    print(">> Delete one from the start/head")
    my_queue.popleft()
    PrintQueue(my_queue)
    print(">> Delete one from the start/head")
    my_queue.popleft()
    PrintQueue(my_queue)
    print(">> Add one on the left")
    my_queue.appendleft(1)
    PrintQueue(my_queue)

    # queue = SimpleQueue()
    # queue.add(0, 'hej')
    # queue.add(1, 'världen')
    # queue.add(2, '!')
    # print(queue)
    # print(queue.pop())
    # print(queue.pop())
    # print(queue.pop())


if __name__ == "__main__":
    main()
