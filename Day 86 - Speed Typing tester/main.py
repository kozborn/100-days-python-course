import time
import tkinter as tk
from email.mime import image
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont

current_word = None
flip_timer = None

BACKGROUND_COLOR = "#B1DDC6"


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("TypeSpeed App")
        self.geometry("800x600")
        self.configure(bg=BACKGROUND_COLOR)
        self.highlight_tags = []

        self.text_field = tk.Text(self, height=10, width=70)
        self.text_field.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.text_field.config(font=("Courier", 12), wrap=tk.WORD)
        self.quote = """A text widget is used for multi-line text area. The tkinter text widget is very powerful and flexible and can be used for a wide range of tasks. Though one of the main purposes is to provide simple multi-line areas, as they are often used in forms, text widgets can also be used as simple text editors or even web browsers."""
        self.user_quote = ""
        self.text_field.insert(tk.END, self.quote)
        self.text_field.config(state=tk.DISABLED)

        self.input_field = tk.Text(self, height=10, width=70)
        self.input_field.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.input_field.config(font=("Courier", 12), wrap=tk.WORD)
        self.input_field.bind("<KeyPress>", self.on_key_press)
        self.input_field.bind("<Delete>", self.on_delete)
        self.input_field.bind("<BackSpace>", self.on_backspace)
        self.input_field.bind("<Return>", self.on_enter)

        self.input_field.focus()

        self.label = tk.Label(self, text="Typing speed: 0 CPM")
        self.label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.label.config(font=("Courier", 22), bg=BACKGROUND_COLOR)
        self.label.config(fg="black")
        self.start_time = None
        self.char_count = 0

    def on_enter(self, event):
        pass

    def on_backspace(self, event):
        cursor_index = self.input_field.index(tk.INSERT)
        prev_index = self.input_field.index(cursor_index + " - 1c")
        self.text_field.tag_remove("green", prev_index, cursor_index)
        self.text_field.tag_remove("red", prev_index, cursor_index)

    def on_delete(self, event):
        cursor_index = self.input_field.index(tk.INSERT)
        self.text_field.tag_remove("green", cursor_index, tk.END)
        self.text_field.tag_remove("red", cursor_index, tk.END)

    def on_key_press(self, event):
        # Check if the pressed key is a letter or space
        cursor_index = self.input_field.index(tk.INSERT)
        if event.char and event.char.isprintable():
            self.char_count += 1
            if self.start_time is None:
                self.start_time = time.time()

            print(
                "Key pressed:",
                event.char,
                " Quote char: ",
                self.text_field.get(cursor_index, cursor_index + " + 1c"),
            )

            self.text_field.tag_config("green", background="green")
            self.text_field.tag_config("red", background="red")

            if event.char == self.text_field.get(cursor_index, cursor_index + " + 1c"):
                self.text_field.tag_add("green", cursor_index, f"{cursor_index} + 1c")
            else:
                self.text_field.tag_add("red", cursor_index, f"{cursor_index} + 1c")

            self.label.config(
                text=f"Typing speed: {int(self.char_count / (time.time() - self.start_time) * 60)} CPM"
            )

            self.compare()

    def compare(self):
        if self.text_field.get("1.0", tk.END) == self.input_field.get("1.0", tk.END):
            messagebox.showinfo("Success", "You typed the text correctly!")


app = App()
app.mainloop()
