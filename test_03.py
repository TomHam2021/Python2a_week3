from collections import deque

plates = deque()
plates.append("One plate")
plates.append("Another plate")
plates.append("A third plate")

print("\n", plates)

# raderar fån vänster till höger
print(plates.popleft())
print(plates.popleft())
print(plates.popleft())

# raderar från höger till vänster (samma som för list)
# print(plates.pop())
# print(plates.pop())
# print(plates.pop())


'''
https://www.geeksforgeeks.org/deque-in-python/

Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in the cases 
where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity 
for append and pop operations as compared to list which provides O(n) time complexity.

* append() :- This function is used to insert the value in its argument to the right end of deque.
* appendleft() :- This function is used to insert the value in its argument to the left end of deque.
* pop() :- This function is used to delete an argument from the right end of deque.
* popleft() :- This function is used to delete an argument from the left end of deque. 

'''
