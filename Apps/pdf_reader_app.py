import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
# Create a canvas of specific size
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3) # Divide canvas into equal columnspan

# Logo
logo = Image.open("./logo.png")
logo = ImageTk.PhotoImage(logo)

root.mainloop()