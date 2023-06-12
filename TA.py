import json

a = {'name': 'Eli', 'age': '25'}
# c={'ali':'reza'}
# with open('sample.json', 'w') as handle:
#     json.dump(a,handle)

with open('sample.json', 'r') as p:
    data = json.load(p)
print(data.get('name'))
# b=json.dumps(c)
