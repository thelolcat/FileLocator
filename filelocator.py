import os

text = ""
current_dir = os.path.abspath(os.getcwd())
files = os.listdir()
dirlist = []
loop : bool

def find():
        files = os.listdir()
        for file in files:
                if file.contains(text):
                        print(os.path.abspath(file))
                if os.path.isdir(file):
                        dirlist.append(os.path.abspath(file))
        nextdir()

def nextdir():
        if dirlist.len() != 0:
                os.chdir(dirlist.pop(0))
                find(text)
        else:
                os.chdir(current_dir)
                print("--------")

while loop:
        text = input("FileLocator >> ")
        if text != "":
                find()
        else:
                break
