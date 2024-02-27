"""FileLocator. Smaller, but still as slow as the default file searcher you get in your system
Trust me, you shouldn't use this in your root folder
I wonder why I built this... -thelolcat"""
import os

text: string
current_dir = os.path.abspath(os.getcwd())
dirlist = []
LOOP = 1


def find():
    """examines files in a folder and checks if it contains "text" (NOT CASE SENSITIVE)"""
    files = os.listdir()
    for file in files:
        if text.lower() in file.lower():
            print(os.path.abspath(file))
        if os.path.isdir(file):
            dirlist.append(os.path.abspath(file))
    nextdir()


def nextdir():
    """changes cwd to next folder to be examined and changes cwd to original folder 
    once search is fully completed"""
    dirloop = 1
    while len(dirlist) != 0 and dirloop == 1:
        try:
            os.chdir(dirlist.pop(0))
            find()
            break
        except PermissionError:
            pass
    if len(dirlist) == 0:
        os.chdir(current_dir)

print("FileLocator loaded. Enter file to be searched(not case sensitive) or enter blank to exit")
while LOOP == 1:
    text = input("FileLocator >> ")
    if text != "":
        find()
        print("----------------")
    else:
        break
