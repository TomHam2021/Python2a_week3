'''
Hash functions
• A hash function takes an object (often a string) as argument and returns a number
• The same object should result in the same number
• Different objects ideally result in different numbers
• Python has a built-in hash function
• It produces unique numbers for each python session
'''

# print(hash("puppy"))
# print(hash("kitty"))
# print(hash("puppy"))


data = list(range(5))           # [0,1,2,3,4]
print(data)


def get_index(key):
    return hash(key) % len(data)


key, value = "puppy", "cute"
x = get_index(key)
print(x)
data[x] = value
print(data[get_index(key)])
