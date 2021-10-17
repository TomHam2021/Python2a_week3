import json

services = {"services": [
    {
        "title": "ECU Reset",
        "id": "11"
    }, {
        "title": "Security Access",
        "id": "27"
    }
]}

# with open("services.json", "w") as file:
# json.dump(services, file)

with open("services.json", "r") as file:
    services = json.load(file)

print(type(services))
