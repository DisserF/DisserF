import tkinter as tk
from tkinter import messagebox
import random
import tkinter as tk
from tkinter import *

options = ("taş", "kağıt", "makas")

def play_game():
    player1 = player1_var.get()
    player2 = random.choice(options)
    player2_label.config(text="Player 2: " + player2)

    if player1 == player2:
        result_label.config(text="Beraberlik!")
    elif (player1 == "taş" and player2 == "makas") or (player1 == "kağıt" and player2 == "taş") or (player1 == "makas" and player2 == "kağıt"):
        result_label.config(text="Player 1 kazandı!")
    else:
        result_label.config(text="Player 2 kazandı!")

def play_again():
    player1_var.set("")
    player2_label.config(text="Player 2: ")
    result_label.config(text="Oyun tekrar başlatıldı")
    #messagebox.showinfo("İnfo")
    #messagebox.showinfo(message=str("Thanks for playing!"))

def cikis_mesaji():
    result = messagebox.askquestion("Çıkış", "Oyundan çıkmak istediğinize emin misiniz?")
    if result == 'yes':
        base.quit()

base = tk.Tk()
base.geometry('800x400')
base.title("Taş kağıt makas (version 0.1)")

header_label = tk.Label(base, text="TAŞ KAĞIT MAKAS", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

player1_label = tk.Label(base, text="Player 1 olarak bir seçim girin (taş, kağıt, makas): ")
player1_label.pack()

player1_var = tk.StringVar()
player1_entry = tk.Entry(base, textvariable=player1_var)
player1_entry.pack()

player2_label = tk.Label(base, text="Player 2: ")
player2_label.pack()

play_button = tk.Button(base, text="Oyna", command=play_game)
play_button.pack(pady=10)

result_label = tk.Label(base, text="")
result_label.pack()

play_again_button = tk.Button(base, text="Tekrar Oyna", command=play_again)
play_again_button.pack(pady=10)

exit_button = tk.Button(base, text="Oyundan çıkmak için tıklayın", command=cikis_mesaji)
exit_button.pack(pady=10)


base.mainloop()
