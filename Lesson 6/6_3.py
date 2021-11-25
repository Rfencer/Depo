import itertools as it
import json

with open('users.csv', 'r', encoding='utf-8') as f:
    name_keys = []
    for line in f:
        name_keys.append(' '.join(line.strip().split(',')))

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby_values = []
    list1 = []
    for line in f:
        list1.append(line.strip())
    for x in list1:
        hobby_values.append(x.split(','))

if len(name_keys) >= len(hobby_values):
    hobby_dict = {k: v for k, v in it.zip_longest(name_keys, hobby_values)}
else:
    raise Exception(1)

with open('hobby_dict.json', 'w', encoding='utf-8') as f:
    json.dump(hobby_dict, f, ensure_ascii=False)
