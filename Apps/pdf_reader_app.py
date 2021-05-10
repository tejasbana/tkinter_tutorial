import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
# Create a canvas of specific size
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3) # Divide canvas into equal columnspan

# Read Logo & Display
logo = Image.open("./logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

root.mainloop()