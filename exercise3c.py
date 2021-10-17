import json

with open("services.json", "r") as file:
    services = json.load(file)

for row in services["services"]:
    print(row)
    print(row.get("id"))
    if row.get("id") == "36":
        print(row.get("title"))
