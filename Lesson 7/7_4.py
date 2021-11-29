import os


files_dict = {}
folder = 'size files'
for i in range(10,51,10):
    files_dict[i] = 0

for item in os.scandir(folder):
    prev_key = 0
    for key in files_dict.keys():
        cur_size = item.stat().st_size // (2 ** 10)
        if prev_key < cur_size < key:
            files_dict[key] += 1
            prev_key = key



print(files_dict)


