from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Input entry box
e = Entry(root, width=35, borderwidth=5, bg="black", fg="white")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Default value for entry box
e.insert(0, "Enter Your Name:  ")

# e.get() to get the content of entry
# Get the content of input box after button has been clicked
def gotClicked():
	outpus_string = "Hello " + e.get()
	myLabel = Label(root, text=outpus_string)
	myLabel.pack()

# Define button widget
myButton = Button(root, text="Click Me!", padx=50,
						fg="red", bg="#000000", 
				  		command=gotClicked)
# use of command to call a fuction after a click



root.mainloop()
