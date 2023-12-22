from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image


class ImageResizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Resizer")
        self.master.geometry("600x700")
        self.filename = ""
        Label(self.master, text="Select an image:").pack(pady=10)
        Button(self.master, text="Browse", command=self.browse).pack(pady=5)
        Label(self.master, text="Enter new width:").pack(pady=5)
        self.w = Entry(self.master)
        self.w.pack(pady=5)
        Label(self.master, text="Enter new height:").pack(pady=5)
        self.h = Entry(self.master)
        self.h.pack(pady=5)
        Button(self.master, text="Resize", command=self.resize).pack(pady=10)

    def browse(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select an Image", filetypes=(
            ("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))

    def resize(self):
        if self.filename:
            try:
                image = Image.open(self.filename)
                nw = int(self.w.get())
                nh = int(self.h.get())
                resized_image = image.resize((nw, nh))
                save_filename = filedialog.asksaveasfilename(initialdir="/", title="Save Image As", filetypes=(
                    ("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
                resized_image.save(save_filename)
                self.filename = ""
                self.w.delete(0, END)
                self.h.delete(0, END)
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "An error occurred while resizing the image.")
        else:
            messagebox.showerror("Error", "Please select an image to resize.")


root = Tk()
app = ImageResizer(root)
root.mainloop()
