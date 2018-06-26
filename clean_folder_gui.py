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
#	while not empty:
#		try:
#			file = next(content)
#			label_2 = Label(root, text = file)
#			label_2.pack()
#		except StopIteration as e:

root = Tk()
ment = StringVar()

root.title("Test Gui App")
root.configure(background = 'white')
root.geometry("450x100")
#root.pack(fill="both", expand = True)

#text box label
label_1_frame = Frame(root)
label_1_frame.pack(fill = X)

label_1 = Label(label_1_frame, text = 'Folder Path', width = 12, relief = RAISED, padx=5, pady=5)
label_1.pack(side = LEFT)

#text box
text_box = Entry(label_1_frame, text='path to folder', textvariable= ment).pack(fill = X, padx=5, pady=5)

buttons_frame= Frame(root)
buttons_frame.pack(fill = X, expand = True)

submit = Button(buttons_frame, text = 'Submit', command = get_path,
					fg = 'white', bg = 'green',
                                        relief = RAISED, padx= 5, pady = 5)
submit.pack(side = LEFT)

exit_button = Button(buttons_frame, text = "Quit", fg = 'black',
					bg = 'yellow', command = root.destroy,
                                        relief = RAISED)
exit_button.pack(side = RIGHT)

#instantiate the gui app
root.mainloop()
