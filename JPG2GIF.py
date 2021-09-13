from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("Image Conversion")

def jpg_to_gif():
    global iml
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".jpg"):
        iml = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension = ".gif")
        iml.save(export_filename)
        messagebox.showinfo("success ", "image conversion was a success")
    else:
        label = Label(root, text="error!", width=20, fg="red", font=("bold", 15))
        label.place(x=80, y=280)
        messagebox.showerror("fail!!", "somthing went wrong...")

def gif_to_jpg():
    global iml
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".gif"):
        iml = Image.open(import_filename).convert('RGB')
        export_filename = fd.asksaveasfilename(defaultextension=".jpg")
        iml.save(export_filename)
        messagebox.showinfo("success ", "image conversion was a success")
    else:
        messagebox.showerror("fail!!", "somthing went wrong...")

button = Button(root, text="JPG to GIF", fg="white",
                width=20, height=2, bg="green",
                font=("helvatica", 12, "bold"),
                command=jpg_to_gif)
button.place(x=120, y=120)

button1 = Button(root, text="GIF to JPG", fg="white",
                width=20, height=2, bg="green",
                font=("helvatica", 12, "bold"),
                command=gif_to_jpg)
button1.place(x=120, y=220)
root.geometry("500x500+400+200")
root.mainloop()