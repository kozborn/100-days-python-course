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
        self.input_field.bind("<KeyRelease>", self.on_key_release)
        self.input_field.focus()

    def on_key_press(self, event):
        # Check if the pressed key is a letter or space
        print("Key pressed:", event.char)
        current_index = f"1.0 + {len(self.input_field.get('1.0', tk.END).strip())}c"
        print("Current index:", current_index)
        self.text_field.tag_remove("highlight", "1.0", tk.END)
        self.text_field.tag_add("highlight", "1.0", current_index)
        self.text_field.tag_config("highlight", background="yellow")

    def on_key_release(self, event):
        # Check if the released key is a letter or space
        pass
        # if event.char.isalpha() or event.char == " " or not event.char:
        #     self.text_field.tag_remove("highlight", "1.0", tk.END)
        #     self.text_field.tag_config("highlight", background="white")


app = App()
app.mainloop()
