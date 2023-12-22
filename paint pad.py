import tkinter as tk
from tkinter import *


class PaintApp:

    def _init_(self, root):
        self.root = root
        self.root.title("MS Paint Clone")

        self.color = "black"
        self.width = 5
        self.draw_mode = "line"
        self.canvas = tk.Canvas(self.root, bg="white", width=500, height=500)
        self.canvas.pack(side=tk.TOP, padx=5, pady=5)

        # Button to change color
        color_btn = tk.Button(self.root, text="Color", command=self.choose_color)
        color_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Button to change line width
        width_btn = tk.Button(self.root, text="Width", command=self.choose_width)
        width_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Button to change draw mode
        mode_btn = tk.Button(self.root, text="Mode", command=self.choose_mode)
        mode_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Button to clear canvas
        clear_btn = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def choose_color(self):
        self.color = tk.colorchooser.askcolor()[1]

    def choose_width(self):
        self.width = tk.simpledialog.askinteger("Width", "Enter line width (1-10)", initialvalue=self.width, minvalue=1,
                                                maxvalue=10)

    def choose_mode(self):
        if self.draw_mode == "line":
            self.draw_mode = "rectangle"
        else:
            self.draw_mode = "line"

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        if self.draw_mode == "line":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=self.width, fill=self.color)
        else:
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, width=self.width,
                                         fill=self.color)

    def end_draw(self, event):
        pass


if __name__ == "_main_":
    root = tk()
    app = PaintApp(root)
    root.mainloop()
