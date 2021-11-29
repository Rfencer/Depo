import os
import shutil

folder = r'manual_my_project/my project'

for root, dirs, files in os.walk(folder):
    new_folder = os.path.join('myproject', 'templates')
    if 'templates' in dirs:
        shutil.copytree(os.path.join(root, 'templates'), new_folder, dirs_exist_ok=True)
