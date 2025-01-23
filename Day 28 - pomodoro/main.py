import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✅"
iteration = 0
timeout = 1000
completed_pomodoro = 0
pomodoro_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global iteration, completed_pomodoro
    completed_pomodoro = 0
    iteration = 0
    if pomodoro_timer:
        window.after_cancel(pomodoro_timer)
    checkmark_text(completed_pomodoro)
    time_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=str(format_count(0)))

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def get_timer(it):
    if it % 2 != 0:
        return WORK_MIN
    elif it % 8 == 0:
        return LONG_BREAK_MIN
    elif it % 2 == 0:
        return SHORT_BREAK_MIN


def checkmark_text(completed_pomodoro):
    text = ""
    for _ in range(completed_pomodoro):
        text += f"{CHECKMARK}"

    return text

def start_timer():
    global iteration, pomodoro_timer
    iteration += 1

    if iteration % 2 != 0:
        time_label.config(text="Work", fg=GREEN)
    elif iteration % 8 == 0:
        time_label.config(text="Long Break", fg=RED)
    elif iteration % 2 == 0:
        time_label.config(text="Short Break", fg=PINK)

    start_count = get_timer(iteration) * 60
    pomodoro_timer = window.after(timeout, count_down, start_count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def format_count(count):
    minutes, seconds = divmod(count, 60)
    return f"{minutes:02}:{seconds:02}"

def count_down(count):
    global completed_pomodoro, iteration, pomodoro_timer
    canvas.itemconfig(timer_text, text=str(format_count(count)))
    if count > 0:
        pomodoro_timer = window.after(timeout, count_down, count - 1)
    else:
        if iteration == 1 or iteration % 2 != 0:
            completed_pomodoro += 1
            checkmark_label.config(text=checkmark_text(completed_pomodoro))
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)

# TOP LABEL
time_label = tk.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
time_label.grid(row=0, column=1)

# POMODORO

bg = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(window, width=203, height=233, bg=YELLOW, borderwidth=0, highlightthickness=0)
canvas.create_image(103, 112, image=bg)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="#fff")
canvas.grid(row=1, column=0, columnspan=3)

# BUTTONS
start_bt = tk.Button(window, text="Start", command=start_timer)
start_bt.grid(row=2, column=0)

reset_bt = tk.Button(window, text="Reset", command=reset_timer)
reset_bt.grid(row=2, column=2)

# CHECKMARKS

checkmark_label = tk.Label(text="", font=(FONT_NAME, 45, "normal"), fg=GREEN, bg=YELLOW, padx=20, pady=25)
checkmark_label.grid(row=2, column=1)

window.mainloop()