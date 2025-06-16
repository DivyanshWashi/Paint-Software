import tkinter as tk

def paint(event):
    x, y = event.x, event.y
    r = brush_size.get()
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=current_color, outline=current_color)

def change_color(color):
    global current_color
    current_color = color

def change_brush_size(size):
    global brush_size
    brush_size = size

# Create main window
root = tk.Tk()
root.title("Simple Drawing App")

# Canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Color buttons
colors = ["red", "green", "blue", "black","pink","yellow","brown","violet","indigo","orange","white","magenta","gold","silver","olive"]
for color in colors:
    btn = tk.Button(root, bg=color, width=4, height=2, command=lambda c=color: change_color(c))
    btn.pack(side=tk.LEFT)

# Brush size scale
brush_size = tk.IntVar(value=5)
scale = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, variable=brush_size, label="Brush Size")
scale.pack()

# Bind mouse events
canvas.bind("<B1-Motion>", paint)

# Default color
current_color = "black"

root.mainloop()
