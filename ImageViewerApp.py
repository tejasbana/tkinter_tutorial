from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images, Exit buttons")

image_list = []

for i in range(1,4):

	# Load and Display Image: 3 steps
	my_img = ImageTk.PhotoImage( Image.open("./images/"+ str(i) + ".png"))
	# my_label = Label(image=my_img)
	# my_label.pack()

	image_list.append(my_img)

my_label = Label(image=image_list[0])
my_label.pack()


# Exit Buttons
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()