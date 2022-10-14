import os
from tkinter import *
from tkinter import filedialog
from datetime import datetime


def rename_files():
    folder = filepath_label.cget("text")
    files = os.listdir(folder)

    for file in files:
        source = f"{folder}/{file}"
        time_modified = os.path.getmtime(source)
        time_created = os.path.getctime(source)

        if time_modified < time_created:
            unix_timestamp = time_modified
        else:
            unix_timestamp = time_created

        date = datetime.utcfromtimestamp(unix_timestamp).strftime("%Y-%m-%d_%H%M%S")
        file_extension = file.split(".")
        new_file_name = f"{date}.{file_extension[-1]}"
        if os.path.exists(f"{folder}/{new_file_name}"):
            number = 1
            while os.path.exists(f"{folder}/{new_file_name}"):
                new_file_name = f"{date}-{number}.{file_extension[-1]}"
                number += 1
            os.rename(source, f"{folder}/{new_file_name}")
        else:
            os.rename(source, f"{folder}/{new_file_name}")


def get_directory():
    filepath = filedialog.askdirectory(initialdir="C:/Users/Pat", title="Select folder")
    filepath_label.config(text=filepath)


# UI
window = Tk()
window.title("Rename Files")
window.config(padx=50, pady=50, bg="#2d2a2e")

instruction_label = Label(text="Choose a folder", bg="#2d2a2e", fg="white", font=("Montserrat", 12, "bold"))
instruction_label.grid(column=0, row=0, columnspan=2)

filepath_label = Label(text="click 'Select'", bg="#524c54", fg="white")
filepath_label.grid(column=0, row=1, columnspan=2)

directory_btn = Button(text="Select", border=0, padx=4, pady=4, command=get_directory)
directory_btn.grid(column=0, row=2, padx=15, pady=15)

rename_btn = Button(text="Rename files", command=rename_files)
rename_btn.grid(column=1, row=2, padx=15, pady=15)


window.mainloop()