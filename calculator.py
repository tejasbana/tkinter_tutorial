from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Input entry box
e = Entry(root, width=35, borderwidth=5, bg="black", fg="white")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Default value for entry box
# e.insert(0, "Enter")

def button_add():
	return

# Define button widget
button_1 = Button(root, text="1", command=button_add)
button_2 = Button(root, text="2", command=button_add)
button_3 = Button(root, text="3", command=button_add)
button_4 = Button(root, text="4", command=button_add)
button_5 = Button(root, text="5", command=button_add)
button_6 = Button(root, text="6", command=button_add)
button_7 = Button(root, text="7", command=button_add)
button_8 = Button(root, text="8", command=button_add)
button_9 = Button(root, text="9", command=button_add)
button_0 = Button(root, text="0", command=button_add)



myButton = Button(root, text="Click Me!", padx=50,
						fg="red", bg="#000000", 
				  		command=gotClicked)
# use of command to call a fuction after a click



root.mainloop()
