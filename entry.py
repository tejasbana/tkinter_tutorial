from tkinter import *

root = Tk()

def gotClicked():
	myLabel = Label(root, text="Just got clicked!")
	myLabel.pack()

# Define button widget
myButton = Button(root, text="Click Me!", padx=50,
						fg="red", bg="#000000", 
				  		command=gotClicked)
# use of command to call a fuction after a click
myButton.pack()

root.mainloop()
