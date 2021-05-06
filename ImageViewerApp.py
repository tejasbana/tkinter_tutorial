from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images, Exit buttons")

# Load Icons 
# root.iconbitmap('./icon/chameleon.ico')


# Load and Display Image: 3 steps
my_img = ImageTk.PhotoImage( Image.open("./icon/chameleon.png"))
my_label = Label(image=my_img)
my_label.pack()



# Exit Buttons
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()