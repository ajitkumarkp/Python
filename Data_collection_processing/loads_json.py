# loads (load from string)takes a json-formatted string input and returns a list or dictionary
import json
a_string = '\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")

print(type(d))
print(d.values())
print(d['resultCount'])

print(d['results'][0]["collectionId"])