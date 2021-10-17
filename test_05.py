# Using a set
# • In mathematics, a set is a collection of distinct objects
# • The syntax for sets in Python is similar to dictionaries
# • You can think of a set as a dictionary with only keys
# • It’s allowed to add the same item twice, but the
#   second time won’t have any effect

unique_stuff = {3, 1, 3}
unique_stuff.add(7)
unique_stuff.add(7)
# print(unique_stuff)

# Set operations
# • You can get the union, intersection and difference of
#   two sets
# • A.union(B) or A | B
# • A.intersection(B) or A & B
# • A.difference(B) or A - B
# • A.symmetric_difference(B) or A ^ B

setA = {1, 3, 3}
setB = {3, 7}
print(setA & setB)  # visa vad som är samma i båda
print(setA ^ setB)  # visa vad som skiler, dvs ta bort alla som finns i båda
print(setA - setB)  # vad uikt finns kvar i A om man tar bort alla lika i B
print(setA | setB)  # om man lägger ihop a+b (unikt)
