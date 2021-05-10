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

# Instruction 
instruction = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instruction.grid(columnspan=3, column=0, row=1)

# Browse Button with variable text message
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway")
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


root.mainloop()