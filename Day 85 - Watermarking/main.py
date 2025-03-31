import tkinter as tk
from email.mime import image
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont

current_word = None
flip_timer = None

BACKGROUND_COLOR = "#B1DDC6"

# window = tk.Tk()
# window.title("Watermarking App")
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas = tk.Canvas(
#     window,
#     width=800,
#     height=526,
#     bg=BACKGROUND_COLOR,
#     borderwidth=0,
#     highlightthickness=0,
# )

# word_text = canvas.create_text(400, 300, text="Test", font=("COURIER", 60, "bold"))
# canvas.grid(row=0, column=0, columnspan=2)
# file_input_button = tk.Button(
#     window,
#     text="Select File",
#     command=askopenfilename,
# )

# file_input_button.grid(row=1, column=0)
# window.mainloop()


def resize_with_aspect_ratio(image, target_width=None, target_height=None):
    original_width, original_height = image.size

    if target_width and not target_height:
        # Resize based on width
        aspect_ratio = original_width / original_height
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    elif target_height and not target_width:
        # Resize based on height
        aspect_ratio = original_width / original_height
        new_width = int(target_height * aspect_ratio)
        new_height = target_height
    else:
        raise ValueError("Specify either target_width or target_height, not both.")

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Watermarking App")
        self.geometry("800x600")
        self.configure(bg=BACKGROUND_COLOR)

        self.canvas = tk.Canvas(
            self,
            width=800,
            height=526,
            bg=BACKGROUND_COLOR,
            borderwidth=0,
            highlightthickness=0,
        )
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.file_input_button = tk.Button(
            self,
            text="Select File",
            command=self.select_file,
        )
        self.file_input_button.grid(row=1, column=0)
        self.image_holder = None

    def select_file(self):
        """Handle file selection and display watermarked image."""
        filename = askopenfilename()
        if filename:
            # Load and resize the selected image
            image = Image.open(filename)
            resized_image = resize_with_aspect_ratio(image=image, target_width=400)

            # Convert watermarked image to Tkinter-compatible format
            watermarked_preview = resized_image.copy()
            draw_on_preview = ImageDraw.Draw(watermarked_preview)

            # Add watermark text (customize font size and position)
            text_position = (10, 10)  # Top-left corner
            draw_on_preview.text(
                text_position, "Sample Watermark", fill=(255, 255, 255, 128)
            )

            # Store reference to prevent garbage collection
            self.watermarked_image_holder = ImageTk.PhotoImage(watermarked_preview)
            self.oryginal_image_holder = image

            # Display the original image on the canvas
            self.image_holder = ImageTk.PhotoImage(resized_image)
            self.canvas.create_image(400, 263, image=self.image_holder, anchor="e")

            # Display the watermarked image on the canvas

            self.canvas.create_image(
                400, 263, image=self.watermarked_image_holder, anchor="w"
            )

            # Create a watermark on the oryginal image
            watermarked_image = image.copy()
            draw = ImageDraw.Draw(watermarked_image)

            # Add watermark text (customize font size and position)
            text_position = (10, 10)  # Top-left corner
            draw.text(text_position, "Sample Watermark", fill=(255, 255, 255, 128))
            # Save the watermarked image
            watermarked_image.save("watermarked_image.png")
            # Display a message box to confirm the watermarking
            messagebox.showinfo(
                "Watermarking Complete",
                "The image has been watermarked and saved as 'watermarked_image.png'.",
            )


app = App()
app.mainloop()

# chancarjacekchanek
# chancarjacekchanek
