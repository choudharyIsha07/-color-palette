import tkinter as tk
from tkinter import filedialog
import random
from PIL import Image, ImageTk

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    return color

def generate_palette():
    num_colors = int(select_field.get())
    for widget in color_frame.winfo_children():
        widget.destroy()
    for i in range(num_colors):
        color = generate_color()
        color_label = tk.Label(color_frame, bg=color, width=10, height=5)
        color_label.grid(row=i, column=0, padx=5, pady=5)
        hex_label = tk.Label(color_frame, text=color, width=10)
        hex_label.grid(row=i, column=1, padx=5, pady=5)

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)

        # Remove previous image label, if exists
        for widget in image_frame.winfo_children():
            widget.destroy()

        img_label = tk.Label(image_frame, image=img_tk)
        img_label.image = img_tk
        img_label.pack()
        img_label.bind("<Button-1>", lambda event: extract_color(img, event.x, event.y))

        # Remove previous extracted color label, if exists
        for widget in color_frame.winfo_children():
            widget.destroy()

def extract_color(img, x, y):
    try:
        pixel = img.getpixel((x, y))
        color = f'#{pixel[0]:02x}{pixel[1]:02x}{pixel[2]:02x}'
        color_label = tk.Label(color_frame, text=f'Extracted Color: {color}', bg=color, width=20, height=2)
        color_label.pack()
    except IndexError:
        pass

root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("400x700")

select_field = tk.StringVar(value="1")
select = tk.OptionMenu(root, select_field, "1", "2", "3", "4", "5")
select.pack(side="top", pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_palette)
generate_button.pack(side="top")

load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(side="top", pady=10)

color_frame = tk.Frame(root)
color_frame.pack(pady=10)

image_frame = tk.Frame(root)
image_frame.pack(pady=10)

root.mainloop()
