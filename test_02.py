plates = []
plates.append("First plate")
plates.append("Another plate")
plates.append("A third plate")

# detta går också men då måste hela listan shiftas till höger för varje appen
# plates.insert(0, "First plate")
# plates.insert(0, "Another plate")
# plates.insert(0, "A third plate")

print("\n", plates)
# The pop() method removes the element at the specified position.
# print(plates.pop(1))  obs index börjar på 0
# print(plates)

# print(plates.pop())   # raderar från höger till vänster
# print(plates.pop())   # .. om inget index så tas det sista elementet bort
# print(plates.pop())

print(plates.pop(0))    # raderar från vänster till höger
print(plates.pop(0))
print(plates.pop(0))
