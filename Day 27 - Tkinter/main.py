import tkinter as tk

window = tk.Tk()
window.title("First GUI Application")
window.minsize(width=400, height=400)

#Label
label = tk.Label(text="Hello World!", font=("Courier", 20, "normal"))
# label.place(x=50, y=50)
label['text'] = "Not so Hello World!"
label.config(text="And again hello")
label.grid(column=0, row=0)
#Button
button = tk.Button(text="Close", command=window.destroy)
# button.pack(side="bottom" )
button.grid(column=1, row=1)
#Input
input = tk.Entry(width=10)
input.grid(column=1, row=0)
# input.pack(side="bottom")

def change_label():
    label['text'] = input.get()

button = tk.Button(text="Print something", command=change_label)
button.grid(column=0, row=1)
# button.pack(side="bottom")




window.mainloop()