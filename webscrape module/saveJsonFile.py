import simplejson as json
from tkinter import filedialog
from tkinter import *

def saveFile(finalMainAnswer):
    root = Tk()
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("json file","*.json"),("all files","*.*")))
    with open(root.filename+".json","w") as newFile:
            json.dump(finalMainAnswer, newFile, indent = 4)

    print("File Created!")

