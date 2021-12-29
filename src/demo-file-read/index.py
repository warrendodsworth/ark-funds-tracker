import json

obj = {'name': 'Warren'}


# json.dump(obj, open('dump.json'))
t = json.dumps(obj, indent=2, sort_keys=True)

f = open('data.json', 'w')
f.write(t)

# print(f.readlines().)
f.close()

# header, output = client.request('', method="GET", body=None,  headers=None)
