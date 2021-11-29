import os

project_path = {'my project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for k, v in project_path.items():
    if os.path.exists(k):
        print("already exists")
    else:
        for x in v:
            os.makedirs(os.path.join(k, x))
