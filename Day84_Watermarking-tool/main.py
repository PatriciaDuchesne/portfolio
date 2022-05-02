import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageDraw, ImageFont

PINK = "#fb575b"
BLUE = "#5fbffd"
NEUTRAL = "#fff8f0"


def open_img():
    img_name = filedialog.askopenfilename(title="Select A File", filetypes=[('image files', ('.png', '.jpg'))])
    img = Image.open(img_name).convert("RGBA")
    return img, img_name


def watermark_img():
    img, name = open_img()
    width, height = img.size
    draw = ImageDraw.Draw(img)
    text = "@oohbhoy"

    font = ImageFont.truetype("C:\Windows\Fonts\Montserrat\Montserrat-Medium.ttf", 36)
    textwidth, textheight = draw.textsize(text, font)

    margin = 15
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font)
    img.save(f'{name}_WATERMARKED.png')

    messagebox.showinfo(title="Success", message="Image has been saved successfully.")


window = tk.Tk()
window.title('Watermarking tool')
window.config(padx=50, pady=50, bg=NEUTRAL)

watermark_label = tk.Label(window, text="Which file do you want to watermark?", font=("Montserrat", 18, "bold"), bg=NEUTRAL, fg=PINK)
watermark_label.grid(column=1, row=0, padx=50, pady=30)

watermark_btn = tk.Button(window, text='Select file', font=("Montserrat", 12, "bold"), bg=BLUE, fg="white", borderwidth=0, command=watermark_img)
watermark_btn.grid(column=1, row=1, padx=25, pady=25)

window.mainloop()
