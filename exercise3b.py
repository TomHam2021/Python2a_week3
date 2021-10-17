'''
Description
If you have taken the Python 1 course, you will recognize the following function. It removes objects with matching name properties.
'''


class Friend:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number


list_of_friends = [
    Friend("Awesome", "Person", "+ 467012345678"),
    Friend("Awesome", "Person", "+ 4681234567"),
    Friend("Bad", "Pal", "+ 46701112233"),
    Friend("Bad", "Pal", "+46 8 111222")
]


def print_friends():
    print("\n>> Friends in the list:")
    for n in list_of_friends:
        print(n.first_name, " ", n.last_name, " ", n.phone_number)


def remove_friend(first, last):
    for friend in list(list_of_friends):
        if friend.first_name == first and friend.last_name == last:
            list_of_friends.remove(friend)
            print(f"Succesfully removed {first} {last}")

# print_friends()
# remove_friend("Bad", "Pal")
# print_friends()
# print()


dict_of_friends = {
    ("Awesome", "Person"): [
        Friend("Awesome", "Person", "+467012345678"),
        Friend("Awesome", "Person", "+4681234567")
    ],
    ("Bad", "Pal"): [
        Friend("Bad", "Pal", "+46701112233"),
        Friend("Bad", "Pal", "+468111222")
    ]
}


def print_friends_dict():
    print("\n>> Friends in the list:")
    for n in dict_of_friends.values():
        for m in n:
            print(m.first_name, " ", m.last_name, " ", m.phone_number)


def remove_friend_dict(first, last):
    if (first, last) in dict_of_friends:
        del dict_of_friends[first, last]
        print(f"Successfully removed {first} {last}")


print_friends_dict()
remove_friend_dict("Bad", "Pal")
print_friends_dict()
