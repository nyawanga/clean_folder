from tkinter import *
import tkinter as tk
import sys
import os
import clean_tkinter

def print_dir_content(path):
    os.chdir(path)
    dir = os.listdir()
    for i in dir:
        yield i

def get_path():
    path_text = ment.get()
    clean_tkinter.move_files(path_text)
    #content = print_dir_content(path_text)
    #empty = False
#    while not empty:
#        try:
#            file = next(content)
#            label_2 = Label(root, text = file)
#            label_2.pack()
#        except StopIteration as e:
#            empty = True

root = Tk()
ment = StringVar()

root.geometry("450x300")
root.title("Test Gui App")
#root.pack(fill="both", expand = True)

label_1 = Label(root, text = 'My Label').pack()

button = Button(root, text = 'Submit', command = get_path, 
                 fg = 'black', bg = 'yellow').pack()

text_box = Entry(root, text='path to folder', textvariable=ment).pack()

exit_button = Button(root, text = "Quit", fg = 'black',
                 bg = 'red', command = root.destroy).pack()

#instantiate the gui app
root.mainloop()
