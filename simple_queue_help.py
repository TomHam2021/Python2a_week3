from typing import Any


class Node:
    # <-Next/Value/Prev->
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class SimpleQueue:
    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, value):
        # Append adds a new node to end of the queue
        new_node = Node(value)

        if self._head:
            # denna if sats körs om self._head är 'nånting' (TRUE)
            # det är den inte första gången!
            # obs att new_node hamnar till höger om sista noden = kö, samma som list
            # <-Next/Value/Prev->
            # new_node becomes the new tail
            new_node.next = self._tail  # den gamla hamnar före/till vänster om new_node
            new_node.prev = None        # det finns ingen Node till höger om new_node

            # replaces references in previous tail, note still same next reference
            self._tail.prev = new_node
            # denna behövs egentligen inte eftersom den inte ändras
            self._tail.next = self._tail.next

            # Update tail to the new_node
            self._tail = new_node

        else:
            # denna körs bara första gången
            # här blir new_node både head & tail
            # No nodes currently exist in the queue
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


def PrintQueue(SimpleQueue):
    current_node = my_queue._head
    while current_node.prev != None:    # loopa tills det inte finns något mer till höger
        print(f"This is the value of our node: {current_node.value}")
        current_node = current_node.prev


my_queue = SimpleQueue()

nr_nodes = 3  # Change this if you append more/less nodes than 3
my_queue.append(0)  # number value is not relevant
my_queue.append(1)
my_queue.append(2)


print("Entering loop that goes from head -> tail")
PrintQueue(my_queue)
print("Delete one from the end/tail")
my_queue.popleft()
PrintQueue(my_queue)
print("Delete one from the end/tail")
my_queue.popleft()
PrintQueue(my_queue)

# current_node = my_queue._head
# for _ in range(nr_nodes):
#     # Works its way through all the nodes. start at the head
#     print(f"This is the value of our node: {current_node.value}")
#     current_node = current_node.prev

# print("Entering loop that goes from tail -> head")

# current_node = my_queue._tail
# for _ in range(nr_nodes):
#     # Works its way through all the nodes. start at tail
#     print(f"This is the value of our node: {current_node.value}")
#     current_node = current_node.next
