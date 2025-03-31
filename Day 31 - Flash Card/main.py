import tkinter as tk
from email.mime import image

import pandas as pd
from tkinter import messagebox
import pyperclip
import random
import json

current_word = None
flip_timer = None

try:
    words_df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_df = pd.read_csv("./data/french_words.csv")

print(len(words_df))


def accept():
    global current_word, words_df
    words_df = words_df[words_df["French"] != current_word["French"]]
    words_df.to_csv("./data/words_to_learn.csv", index=False)
    print(current_word.to_frame().T)
    try:
        known_words = pd.read_csv("./data/known.csv")
    except FileNotFoundError:
        empty_df = pd.DataFrame()
        df = pd.concat([empty_df, current_word.to_frame().T], ignore_index=True)
        df.to_csv("./data/known.csv", index=False)
    else:
        df = pd.concat([known_words, current_word.to_frame().T], ignore_index=True)
        df.to_csv("./data/known.csv", index=False)
    finally:
        next_card()


def reject():
    print("Rejected")
    next_card()
    pass


def flip_card(word):
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)


def next_card():
    global current_word
    global flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_word = words_df.iloc[random.randint(0, len(words_df))]
    current_word_fr = current_word["French"]
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word_fr, fill="black")
    flip_timer = window.after(2000, flip_card, current_word)


BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = tk.PhotoImage(file="./images/card_front.png")
card_back = tk.PhotoImage(file="./images/card_back.png")
button_right = tk.PhotoImage(file="./images/right.png")
button_wrong = tk.PhotoImage(file="./images/wrong.png")

canvas = tk.Canvas(
    window,
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    highlightthickness=0,
)
card_image = canvas.create_image(400, 263, image=card_front)
lang_text = canvas.create_text(400, 200, text="French", font=("COURIER", 40, "italic"))
word_text = canvas.create_text(400, 300, text="", font=("COURIER", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button = tk.Button(
    window, command=accept, image=button_right, borderwidth=0, highlightthickness=0
)
right_button.grid(row=1, column=1)

wrong_button = tk.Button(
    window, command=reject, image=button_wrong, borderwidth=0, highlightthickness=0
)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()


# chancarjacekchanek
# chancarjacekchanek
