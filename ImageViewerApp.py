from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images, Exit buttons")

image_list = []

for i in range(3):

	# Load and Display Image: 3 steps
	my_img = ImageTk.PhotoImage( Image.open("./images/"+ str(i+1) + ".png"))
	# my_label = Label(image=my_img)
	# my_label.pack()

	image_list.append(my_img)


# Current image index and length of image list


# Display first image
image_label = Label(image=image_list[0])
image_label.grid(row=0, column=0, columnspan=3)


def next_image(image_number):
	global image_label
	global button_next
	global button_prev

	image_label.grid_forget()

	image_label = Label(image=image_list[image_number - 1])
	button_prev = Button(root, text="<<", command=lambda: prev_image(image_number-1))
	button_next = Button(root, text=">>", command=lambda: next_image(image_number+1))

	if image_number == 3:
		button_next = Button(root, text=">>", command=DISABLED)


	image_label.grid(row=0, column=0, columnspan=3)
	button_prev.grid(row=1, column=0)
	button_next.grid(row=1, column=2)


def prev_image():
	global image_label
	global button_next
	global button_prev


# Buttons
button_prev = Button(root, text="<<", command=prev_image)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_next = Button(root, text=">>", command=lambda: next_image(2))

# Display buttons 
button_prev.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)


root.mainloop()