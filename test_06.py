from collections import defaultdict
import random

children = defaultdict(list)    # defalut = list = []
children[1] = ["Emil", "Jonas"]
children[4].append("Pontus")

print(f"{children[1]} have no children")
# koller att få ett defaul värde = [] = list
print(f"{children[2]} have one child")
print(f"{children[4]} have one child")


# print(random.randrange(10))

def my_function():
    return random.randrange(100)


# här kommer det defaul att bli ett random nummer..
numbers = defaultdict(my_function)
print(numbers[0], numbers[1], numbers[2])
