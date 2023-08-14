import os
import shutil

#from_dir and to_dir would change depending on the file(s)
from_dir = "C:/Users/archi/Downloads"
to_dir = "C:/Users/archi/OneDrive/Desktop/WhiteHatJr/Pro C111 Prj/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + "........")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + "........")
            shutil.move(path1, path3)


