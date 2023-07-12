import time
import threading
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def start_timer_thread():
    t = threading.Thread(target=start_timer)
    t.start()
    #root.start_button.config(state="disabled")

def start_timer():
    root.stopped = False
    root.skipped = False
    timer_id = root.tabs.index(root.tabs.select()) + 1
    if timer_id == 1:
        countdown(25*60, root.pomodoro_timer_label)
    elif timer_id == 2:
        countdown(5*60, root.short_break_timer_label)
    elif timer_id == 3:
        countdown(15*60, root.long_break_timer_label)

def reset_clock():
    root.stopped = True
    timer_id = root.tabs.index(root.tabs.select()) + 1
    if timer_id == 1:
        root.pomodoro_timer_label.configure(text="25:00")
    elif timer_id == 2:
        root.short_break_timer_label.configure(text="05:00")
    elif timer_id == 3:
        root.long_break_timer_label.configure(text="15:00")

def stop_clock():
    root.stopped = True
    root.skip_button.configure(text="Devam Et", command=resume_clock)

def resume_clock():
    root.stopped = False
    root.skip_button.configure(text="Durdur", command=stop_clock)
    decrement_time()

def decrement_time():
    if not root.stopped:
        timer_id = root.tabs.index(root.tabs.select()) + 1
        if timer_id == 1:
            label = root.pomodoro_timer_label
        elif timer_id == 2:
            label = root.short_break_timer_label
        elif timer_id == 3:
            label = root.long_break_timer_label

        current_time = label["text"]
        minutes, seconds = map(int, current_time.split(":"))
        total_seconds = minutes * 60 + seconds

        if total_seconds > 0:
            total_seconds -= 1
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            label.configure(text=f"{minutes:02d}:{seconds:02d}")
            root.after(1000, decrement_time)
        else:
            if timer_id == 1:
                root.pomodoros += 1
                root.pomodoro_counter_label.configure(text=f"Pomodoros: {root.pomodoros}")

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

def countdown(seconds, label):
    while seconds > 0:
        if root.stopped:
            return
        if root.skipped:
            label.configure(text="00:00")
            return
        label.configure(text=format_time(seconds))
        time.sleep(1)
        seconds -= 1
    label.configure(text="00:00")
    if root.tabs.index(root.tabs.select()) == 0:
        root.pomodoros += 1
        root.pomodoro_counter_label.configure(text=f"Pomodoros: {root.pomodoros}")

root = tk.Tk()
root.geometry("920x736")
root.title("THT - Pomodoro")
root.iconbitmap("D:\codes/pomodoro/tht1.ico")
root.s = ttk.Style()
root.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
root.s.configure("TButton", font=("Ubuntu", 16))


root.tabs = ttk.Notebook(root)
root.tabs.pack(fill="both", pady=10, expand=True)


root.tab1 = ttk.Frame(root.tabs, width=600, height=100)
root.tab2 = ttk.Frame(root.tabs, width=600, height=100)
root.tab3 = ttk.Frame(root.tabs, width=600, height=100)

background_image = Image.open("D:\codes/pomodoro/tht.png")
background_photo = ImageTk.PhotoImage(background_image)


background_label = tk.Label(root, image=background_photo)
background_label.place(x=250, y=180, width=425, height=363)


root.pomodoro_timer_label = ttk.Label(root.tab1, text="25:00", font=("Ubuntu", 48))
root.pomodoro_timer_label.pack(pady=20)

root.short_break_timer_label = ttk.Label(root.tab2, text="05:00", font=("Ubuntu", 48))
root.short_break_timer_label.pack(pady=20)

root.long_break_timer_label = ttk.Label(root.tab3, text="15:00", font=("Ubuntu", 48))
root.long_break_timer_label.pack(pady=20)

root.grid_layout = ttk.Frame(root)
root.grid_layout.pack(pady=10)

root.start_button = ttk.Button(root.grid_layout, text="Başla", command=start_timer_thread)
root.start_button.grid(row=0, column=0)

root.skip_button = ttk.Button(root.grid_layout, text="Durdur", command=stop_clock)
root.skip_button.grid(row=0, column=1)

root.reset_button = ttk.Button(root.grid_layout, text="Sıfırla", command=reset_clock)
root.reset_button.grid(row=0, column=2)

root.pomodoro_counter_label = ttk.Label(root.grid_layout, text="Pomodoros: 0", font=("Ubuntu", 16))
root.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

root.pomodoros = 0
root.skipped = False
root.stopped = False

root.tabs.add(root.tab1, text="Pomodoro")
root.tabs.add(root.tab2, text="Kısa ara")
root.tabs.add(root.tab3, text="Uzun ara")


root.mainloop()