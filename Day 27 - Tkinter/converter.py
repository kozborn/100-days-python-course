import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

m_input = tk.Entry(width=10)
m_input.grid(column=1, row=0)

m_label = tk.Label(text="Miles")
m_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1, padx=10, pady=10)

result = tk.Label(text="--")
result.grid(column=1, row=1)

km_label = tk.Label(text="km")
km_label.grid(column=2, row=1)




def convert_to_km():
    m_input.get()
    r = float(m_input.get()) * 1.60934
    result.config(text=f"{r:.2f}")

calculate = tk.Button(text="Calculate", command=convert_to_km)
calculate.grid(column=1, row=2)



window.mainloop()
