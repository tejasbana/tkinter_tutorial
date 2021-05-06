from tkinter import *

root = Tk()
root.title("Images, Exit buttons")

# Load Icons 
# root.iconbitmap('icon/chameleon.ico')

# Exit Buttons
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()