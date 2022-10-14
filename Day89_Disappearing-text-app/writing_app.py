from datetime import datetime
import math
import time
import tkinter as tk
from tkinter import messagebox
from typing import Optional

SESSION_MINUTES = 5
SESSION_SECONDS = SESSION_MINUTES * 60
last_key: Optional[float] = None
user_is_typing = False
timer = None


def press_any_key(_event):
    global user_is_typing
    global last_key
    last_key = time.time()
    if not user_is_typing:
        user_is_typing = True
        start_session_timer(SESSION_SECONDS)
        keypress_countdown()


def keypress_countdown():
    global user_is_typing
    window.after(100, keypress_countdown)
    if time.time() - last_key >= 10:
        disappear_text()
        reset_session_timer()
        user_is_typing = False


def start_session_timer(seconds):
    session_sec = seconds % 60
    session_min = math.floor(seconds / 60)
    if session_sec < 10:
        session_sec = f"0{session_sec}"
    timer_label.config(text=f"{session_min}:{session_sec}")
    if seconds > 0:
        global timer
        timer = window.after(1000, start_session_timer, seconds - 1)
    else:
        save_text()


def reset_session_timer():
    window.after_cancel(timer)
    timer_label.config(text="00:00")


def disappear_text():
    text_input.delete("1.0", "end")


def save_text():
    global user_is_typing
    date_and_time = datetime.now().strftime("%Y%m%d-%H%M")
    save = messagebox.askyesno(title="Save", message="Your writing session is finished. \nSave?")
    if save is True:
        with open(f"{date_and_time}.txt", mode="a") as file:
            file.write(text_input.get("1.0", "end"))
    text_input.delete("1.0", "end")
    user_is_typing = False


window = tk.Tk()
window.config(bg="#343739")
window.geometry('1000x800')
window.title('Writing App')

window.bind('<Any-KeyPress>', press_any_key)

timer_label = tk.Label(text="00:00", font=("Arial", 10), bg="#343739", fg="white")
timer_label.pack(padx=(950, 0))

instructions_label = tk.Label(window, justify="center", font=("Arial", 14, "bold"), text="Keep writing. Don't stop.", bg="#343739", fg="#f85555")
instructions_label.pack(pady=15)

text_input = tk.Text(window, width=65, height=42, font=("Arial", 12, "bold"), wrap="word")
text_input.config(background="#343739", foreground="white", borderwidth=0)
text_input.pack(pady=20)


window.mainloop()
