#  dumps() takes a list or dictionary input and returns a json-formatted string

import json

def pretty(dict_or_list_in):
    string_out = json.dumps(dict_or_list_in, sort_keys=True, indent=2)
    return string_out

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')

print(pretty(d))




