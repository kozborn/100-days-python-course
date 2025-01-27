import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = tk.Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white", pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(self.window, background="#fff", height=300, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.question_text = self.canvas.create_text(
            (150, 150),
            width=280,
            text="test",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)

        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(text="", command=self.yes_answer, bg=THEME_COLOR, image=true_image, highlightcolor=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(column=0, row=2, pady=20)

        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(text="", command=self.no_answer, bg=THEME_COLOR, image=false_image, highlightcolor=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def yes_answer(self):
        self.check_answer("True")

    def no_answer(self):
        self.check_answer("False")

    def check_answer(self, answer):
        self.false_button['state'] = tk.DISABLED
        self.true_button['state'] = tk.DISABLED
        if self.quiz_brain.check_answer(answer):
            self.canvas.config(background="#C2FFC7")
            print("Correct!")
            self.quiz_brain.increase_score()

        else:
            self.canvas.config(background="#BE3144")
            self.canvas.itemconfig(self.question_text, fill="white")
            print("Incorrect!")
        self.update_score()
        self.window.after(1000, self.get_next_question)

    def reset_canvas(self):
        self.false_button['state'] = tk.ACTIVE
        self.true_button['state'] = tk.ACTIVE
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")

    def update_question(self, new_question):
        self.canvas.itemconfig(self.question_text, text=new_question)

    def game_result(self):
        self.false_button['state'] = tk.DISABLED
        self.true_button['state'] = tk.DISABLED
        self.canvas.itemconfig(self.question_text, text=f"Game Result: {self.quiz_brain.score}/{len(self.quiz_brain.question_list)}")

    def get_next_question(self):
        self.reset_canvas()
        if self.quiz_brain.still_has_questions():
            self.update_question(self.quiz_brain.next_question())
        else:
            self.game_result()

