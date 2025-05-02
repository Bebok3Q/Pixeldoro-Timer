import tkinter as tk
from tkinter import messagebox, Scale, Toplevel, Label, Entry, Checkbutton, BooleanVar, PhotoImage, font
from datetime import timedelta
from playsound import playsound
import os
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Timer:
    def __init__(self, canvas, text_id):
        self.canvas = canvas
        self.text_id = text_id
        self.running = False
        self.after_id = None

        self.work_duration = timedelta(minutes=25)
        self.break_duration = timedelta(minutes=5)
        self.auto_break_enabled = True
        self.session_type = "work"
        self.timer_time = self.work_duration
        self.initial_time = self.work_duration

    def format_time(self, td):
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"

    def update_timer(self):
        self.canvas.itemconfig(self.text_id, text=self.format_time(self.timer_time))
        if self.timer_time > timedelta(0):
            self.timer_time -= timedelta(seconds=1)
            self.after_id = root.after(1000, self.update_timer)
        else:
            self.running = False
            self.canvas.itemconfig(self.text_id, text="Done!")
            playsound('assets/Sounds/Sound.mp3')
            if self.session_type == "work" and self.auto_break_enabled:
                self.start_break()

    def start_timer(self):
        if not self.running:
            self.session_type = "work"
            self.timer_time = self.work_duration
            self.initial_time = self.work_duration
            self.running = True
            self.update_timer()

    def start_break(self):
        self.session_type = "break"
        self.timer_time = self.break_duration
        self.initial_time = self.break_duration
        self.running = True
        self.update_timer()

    def stop_timer(self):
        if self.running and self.after_id:
            root.after_cancel(self.after_id)
            self.running = False

    def reset_timer(self):
        self.stop_timer()
        self.timer_time = self.initial_time
        self.canvas.itemconfig(self.text_id, text=self.format_time(self.timer_time))

    def preview_time(self, value):
        if not self.running:
            preview_td = timedelta(minutes=int(value))
            self.canvas.itemconfig(self.text_id, text=self.format_time(preview_td))

    def apply_settings(self, work_min, break_min, auto_break):
        try:
            work_minutes = int(work_min)
            break_minutes = int(break_min)
            self.work_duration = timedelta(minutes=work_minutes)
            self.break_duration = timedelta(minutes=break_minutes)
            self.auto_break_enabled = auto_break
            if not self.running:
                self.timer_time = self.work_duration
                self.initial_time = self.work_duration
                self.canvas.itemconfig(self.text_id, text=self.format_time(self.timer_time))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for time.")


def open_settings():
    settings_win = Toplevel(root)
    settings_win.title("Settings")
    settings_win.geometry("250x200")

    Label(settings_win, text="Work Duration (min):").pack(pady=(10, 0))
    work_entry = Entry(settings_win)
    work_entry.insert(0, str(int(t.work_duration.total_seconds() // 60)))
    work_entry.pack()

    Label(settings_win, text="Break Duration (min):").pack(pady=(10, 0))
    break_entry = Entry(settings_win)
    break_entry.insert(0, str(int(t.break_duration.total_seconds() // 60)))
    break_entry.pack()

    auto_break_var = BooleanVar(value=t.auto_break_enabled)
    Checkbutton(settings_win, text="Auto-start Break", variable=auto_break_var).pack(pady=10)

    def save_and_close():
        t.apply_settings(work_entry.get(), break_entry.get(), auto_break_var.get())
        settings_win.destroy()

    tk.Button(settings_win, text="Save", command=save_and_close).pack(pady=5)


# GUI Setup
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("400x550")
root.iconbitmap(resource_path('assets/icon.ico'))

canvas = tk.Canvas(root, width=400, height=550)
canvas.pack(fill="both", expand=True)

bg_image = PhotoImage(file="assets/Images/background_png.png")
canvas.create_image(0, 0, anchor="nw", image=bg_image)

# font_path = r'assets/Fonts/DayDream.ttf'
# custom_font = font.Font(file=font_path, size=24)

text_id = canvas.create_text(200, 120, text="", font=("DayDream",36), fill="#dbd4ca")

# Timer Instance
t = Timer(canvas, text_id)
canvas.itemconfig(text_id, text=t.format_time(t.timer_time))

# Buttons - smaller and in 2x2 grid at bottom
button_width = 10  # Smaller width
button_font = ("DayDream", 10)  # Smaller font

start_button = tk.Button(root, text="Start", command=t.start_timer, width=button_width, font=button_font, bg= '#637FAB', fg= '#CCCCCC',activebackground='#51678A')
stop_button = tk.Button(root, text="Stop", command=t.stop_timer, width=button_width, font=button_font, bg= '#7C5B57', fg= '#CCCCCC',activebackground='#634A47')
reset_button = tk.Button(root, text="Reset", command=t.reset_timer, width=button_width, font=button_font, bg= '#534751', fg= '#CCCCCC',activebackground='#403A40')
settings_button = tk.Button(root, text="Settings", command=open_settings, width=button_width, font=button_font, bg= '#4C485B', fg= '#CCCCCC',activebackground='#3A3645')

# Position buttons in 2x2 grid at bottom
canvas.create_window(100, 450, window=start_button)    # Row 1, Col 1
canvas.create_window(300, 450, window=stop_button)     # Row 1, Col 2
canvas.create_window(100, 500, window=reset_button)    # Row 2, Col 1
canvas.create_window(300, 500, window=settings_button) # Row 2, Col 2

root.mainloop()