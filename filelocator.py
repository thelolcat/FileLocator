import os

text = ""
current_dir = os.path.abspath(os.getcwd())
files = os.listdir()
dirlist = []
LOOP = 1

#examines files in a folder and checks if it contains "text" (NOT CASE SENSITIVE)
def find():
    files = os.listdir()
    for file in files:
        if text.lower() in file.lower():
            print(os.path.abspath(file))
        if os.path.isdir(file):
            dirlist.append(os.path.abspath(file))
    nextdir()


#changes cwd to next folder to be examined and changes cwd to original folder once search is fully completed
def nextdir():
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

print("FileLocator loaded. Enter file to be searched(not case sensitive) or enter blank to exit program")
while LOOP == 1:
    text = input("FileLocator >> ")
    if text != "":
        find()
        print("----------------")
    else:
        break