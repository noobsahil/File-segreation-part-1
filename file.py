import os
import shutil

from_dir = "C:/Users/sahil/OneDrive/Documents" 
to_dir = "C:/Users/sahil/OneDrive/Desktop/-/Python"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name, ext = os.path.splitext(file)
    print(f"File name: {name}, extension: {ext}")
    shutil.move(os.path.join(from_dir, file), os.path.join(to_dir, file))
