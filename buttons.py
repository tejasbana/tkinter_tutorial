from tkinter import *

root = Tk()

def gotClicked():
	myLabel = Label(root, text="Just got clicked!")
	myLabel.pack()

# Define button widget
myButton = Button(root, text="Click Me!", padx=50, command=gotClicked)
myButton.pack()

root.mainloop()
