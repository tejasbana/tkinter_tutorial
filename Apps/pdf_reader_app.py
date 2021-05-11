import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, askopenfilename

root = tk.Tk()
# Create a canvas of specific size
canvas = tk.Canvas(root, width=600, height=300)
# Divide canvas into equal columnspan & rowspan
canvas.grid(columnspan=3, rowspan=3) 

# Read Logo & Display
logo = Image.open("./logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instruction 
instruction = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instruction.grid(columnspan=3, column=0, row=1)

def open_file():
	browse_text.set("Loading...")
	# askopenfile Opens a file and askopenfilename returns filename
	file = askopenfile( mode='rb', filetypes=[("Pdf file", "*.pdf")], parent=root, title="Choose a file")
	# file = askopenfilename(filetypes=[("Pdf file", "*.pdf")])
	# file = askopenfile(parent=root, mode='rb', title="Choose a file",
	# 				                filetype=[("Pdf file", "*.pdf")] )
	if file:
		read_pdf = PyPDF2.PdfFileReader(file)
		page = read_pdf.getPage(0)
		page_content = page.extractText()

		# Text Box
		text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
		text_box.insert(1.0, page_content)
		text_box.tag_configure("center", justify="center")
		text_box.tag_add("center", 1.0, "end")
		text_box.grid(column=1, row=3)

		browse_text.set("Browse")


# Browse Button with variable text message
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway",
					   command=lambda:open_file(),
					   highlightbackground="#20bebe", bg="#20BEBE", fg="Black", height=2, width=15)

browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


# Create a canvas of specific size
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3) 



root.mainloop()