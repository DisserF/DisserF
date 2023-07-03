import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import screen_brightness_control as pct
from textblob import TextBlob
from tkinter import Label

root = Tk()
root.title("Düzelt, konuş ve öğren")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="gray")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()   

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()            

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()   

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()            

def change_brightness():
    level = brightness_entry.get()
    pct.set_brightness(level)
    # Ekstra olarak, güncellenmiş parlaklık değerini görüntüleyebilirsiniz
    print(pct.get_brightness())

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root, text="Correct text is:", font=("poppins", 10), bg="black", fg="white")
    cs.place(x=650, y=120)
    spell.config(text=right)
    spell.place(x=750,y=120)
    

# Top Frame
Top_frame = Frame(root, bg="gray", width=900, height=100)
Top_frame.place(x=0, y=0) # sayfayı çeyrek olarak ayırdı

Logo =tk.PhotoImage(file="D:\codes\speak gelişmiş\speaker.png")
Label(Top_frame, image=Logo, bg="gray").place(x=0, y=0)

Label(Top_frame, text="DÜZELT, KONUŞ VE ÖĞREN", font="arial 20 bold", bg="gray", fg="black").place(x=102, y=35)

text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="SES", font="arial 15 bold", bg="gray", fg="black").place(x=580, y=160)
Label(root, text="HIZ", font="arial 15 bold", bg="gray", fg="black").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

imageicon =tk.PhotoImage(file="D:\codes\speak gelişmiş\speak.png")
btn = Button(root, text="Konuş", compound=LEFT, image=imageicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

imageicon2 =tk.PhotoImage(file="D:\codes\speak gelişmiş\download.png")
save = Button(root, text="Kaydet", compound=LEFT, image=imageicon2, width=130, font="arial 14 bold", command=download)
save.place(x=730, y=280)

# Spelling Checker
heading = Label(root, text="Kelime düzenleyici", font=("Trebuchet MS", 20, "bold"), bg="gray", fg="black")
heading.place(x=610,y=10)

enter_text = Entry(root, justify="center", width=15, font=("poppins", 10), bg="white", border=2)
enter_text.place(x=670,y=60)
enter_text.focus()

button = Button(root, text="Kontrol et", font=("arial", 8, "bold"), fg="white", bg="black", command=check_spelling)
button.place(x=700,y=90)
button.focus()

spell = Label(root, font=("poppins", 10), bg="black", fg="white")
#spell.place(x=350, y=250)

brightness_entry = Entry(root, width=5)
brightness_entry.place(x=710, y=380)

change_button = Button(root, text="Parlaklık (%50)", compound=LEFT, width=20, font="arial 14 bold", command=change_brightness)
change_button.place(x=600, y=400)

# icon
image_icon =tk.PhotoImage(file="D:\codes\speak gelişmiş\speak.png")
root.iconphoto(False, image_icon)

root.mainloop()