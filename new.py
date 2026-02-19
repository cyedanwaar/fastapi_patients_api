import json

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


# print(load_data())

data = load_data()

print(data.keys())
print(data.values())

sorted_data = sorted(data.values(), key=lambda x: x.get())