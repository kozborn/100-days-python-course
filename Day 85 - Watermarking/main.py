import tkinter as tk
from email.mime import image
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont

current_word = None
flip_timer = None

BACKGROUND_COLOR = "#B1DDC6"


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
        self.image = None
        self.watermarked_image = None
        self.filename = None
        self.watermarked_image_preview = None
        self.image_preview = None
        self.canvas = tk.Canvas(
            self,
            width=800,
            height=500,
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
        self.save_button = tk.Button(
            self,
            text="Save Watermarked Image",
            command=self.add_watermark_and_save_file,
        )
        self.save_button.grid(row=1, column=1)

        self.watermark_text_input = tk.Entry(
            self,
            width=75,
        )
        self.watermark_text_input.grid(row=2, column=0, columnspan=2)
        self.watermark_text_input.insert(0, "Enter watermark text here")
        self.watermark_text_input.bind(
            "<Return>", lambda event: self.draw_watermarked_preview()
        )
        self.refresh_button = tk.Button(
            self,
            text="Refresh Preview",
            command=self.draw_watermarked_preview,
        )
        self.refresh_button.config(state="disabled")
        self.refresh_button.grid(row=3, column=1, columnspan=1)

    def add_watermark_and_save_file(self):
        """Handle file saving."""
        if self.image is None:
            messagebox.showwarning("No Image", "Please select an image first.")
            return
        self.watermarked_image = self.image.copy()
        if self.watermarked_image:

            draw = ImageDraw.Draw(self.watermarked_image)

            # Add watermark text (customize font size and position)
            text_position = (10, 10)  # Top-left corner
            draw.text(
                text_position,
                self.watermark_text_input.get(),
                fill=(255, 255, 255, 128),
            )

            save_path = "watermarked_image_" + self.filename.split("/")[-1]
            self.watermarked_image.save(save_path)
            messagebox.showinfo(
                "Save Complete",
                f"The image has been saved as '{save_path}'.",
            )
        else:
            messagebox.showwarning("No Image", "Please select an image first.")

    def select_file(self):
        """Handle file selection and display watermarked image."""
        self.filename = askopenfilename()
        if self.filename:
            # Load and resize the selected image
            self.image = Image.open(self.filename)
            self.resized_image = resize_with_aspect_ratio(
                image=self.image, target_width=400
            )
            self.draw_preview()
            self.draw_watermarked_preview()
            self.refresh_button.config(state="normal")
        else:
            self.refresh_button.config(state="disabled")

    def draw_preview(self):
        """Draw the preview of the original image."""
        self.image_preview = ImageTk.PhotoImage(self.resized_image)
        if self.image_preview:
            self.canvas.delete("original")
            self.canvas.create_image(400, 263, image=self.image_preview, anchor="e")
            self.canvas.tag_lower("original")

    def draw_watermarked_preview(self):
        """Draw the preview of the watermarked image."""
        # Convert watermarked image to Tkinter-compatible format
        watermarked_preview = self.resized_image.copy()
        draw_on_preview = ImageDraw.Draw(watermarked_preview)

        # Add watermark text (customize font size and position)
        text_position = (10, 10)  # Top-left corner
        draw_on_preview.text(
            text_position,
            self.watermark_text_input.get(),
            fill=(255, 255, 255, 128),
        )

        # Display the original image on the canvas

        # Store reference to prevent garbage collection
        self.watermarked_image_preview = ImageTk.PhotoImage(watermarked_preview)
        # Display the watermarked image on the canvas
        if self.watermarked_image_preview:
            self.canvas.delete("watermarked")
            self.canvas.create_image(
                400, 263, image=self.watermarked_image_preview, anchor="w"
            )
            self.canvas.tag_lower("watermarked")


app = App()
app.mainloop()

# chancarjacekchanek
# chancarjacekchanek
