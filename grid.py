from tkinter import *

root = Tk()

# Define Label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Tejas Bana")
emptyLabel = Label(root, text="            ")

# Display using grid system && matrix index are relative
myLabel1.grid(row=0, column=0)
# Trick: for adding space between columns add empty label
emptyLabel.grid(row=1,column=1)
myLabel2.grid(row=1, column=5)


root.mainloop()
