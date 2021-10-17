from typing import Any

# https://realpython.com/lessons/type-hinting/
# om Type Hinting


# detta är en nod
class Node:
    # A node of a doubly linked list has a value and two node references
    # value kan vara av vilken typ som helst "Any" & konstruktorn returnerar inget "None"
    def __init__(self, value: Any) -> None:
        self.value: Any = value                 # betyder att value kan vara vad som helst
        # betyder att prev pekar på inget/None av typen "Node"
        self.prev: Node = None
        self.next: Node = None                  # efter : kommer en hint/tips


# detta är en kö av noder med en head och en tail
class SimpleQueue:
    # A doubly linked list
    def __init__(self) -> None:
        self._head: Node = None
        self._tail: Node = None

    def remove(self, index: int) -> None:
        # Removes node at specified index"""
        node = self._head
        for _ in range(index):              # Find the node with specified index
            node = node.prev
        if node.prev:                       # Removing from middle or at beginning
            node.prev.next = node.next
        if node.next:                       # Removing from middle or end of queue
            node.next.prev = node.prev
        if node == self._head:              # Removing from beginning of queue
            self._head = node.prev
        if node == self._tail:              # Removing from end of queue
            self._tail = node.next

    def add(self, index: int, value: str):
        new_node = Node(value)
        new_node.value = value
        if self._head:  # not empty
            node = self._head
            for _ in range(index):
                node = node.prev
            if node:  # middle or beginning
                if node.next:  # middle
                    node.next.prev = new_node
                    new_node.next = node.next
                else:  # beginning
                    self._head = new_node
                new_node.prev = node
                node.next = new_node
            else:  # end
                new_node.next = self._tail
                self._tail.prev = new_node
                self._tail = new_node
        else:  # queue empty
            self._head = new_node
            self._tail = new_node


testQ = SimpleQueue
testQ.add(1, "Body", "body")
