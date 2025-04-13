import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click = None

        self.canvas.bind("<Motion>", self.update_mouse_position)
        self.canvas.bind("<Button-1>", self.handle_click)

        self.root.update()

    def update_mouse_position(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def handle_click(self, event):
        self.last_click = (event.x, event.y)

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def get_last_click(self):
        return self.last_click

    def wait_for_click(self):
        self.last_click = None
        while self.last_click is None:
            self.root.update()

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

    def set_color(self, object_id, color):
        self.canvas.itemconfig(object_id, fill=color)

    def moveto(self, object_id, x, y):
        coords = self.canvas.coords(object_id)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self.canvas.coords(object_id, x, y, x + width, y + height)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)
