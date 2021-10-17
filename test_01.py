children = {"Emil": 0, "Pontus": 4, "Jonas": 0}     # dictionary
print(children)

for name, number_of_children in children.items():   # name = key, number_of_children = data
    if number_of_children == 0:
        print(f"{name} has no children")
print()
# numbers = key, name = data = list [] , obs att detta ger samma resultat som ovan!
children = {0: ["Emil", "Jonas"], 4: ["Pontus"]}
print(children)

for name in children[0]:
    print(f"{name} has no children")

print()
