import os
import json

files_dict = {}
folder = 'size files'
for i in range(10, 51, 10):
    files_dict[i] = [0, []]

for item in os.scandir(folder):
    prev_key = 0
    for key in files_dict.keys():
        cur_size = item.stat().st_size // (2 ** 10)
        ext = item.name[item.name.rfind('.'):]
        if prev_key < cur_size < key:
            files_dict[key][0] += 1
            if ext not in files_dict[key][1]:
                files_dict[key][1].append(ext)
            prev_key = key

json_dict = {}
for k, v in files_dict.items():
    json_dict[k] = tuple(v)

print(json_dict)

with open(os.path.basename(os.getcwd()) + '_size_files.json', 'w', encoding='utf-8') as f_json:
    json.dump(json_dict, f_json, ensure_ascii=False)