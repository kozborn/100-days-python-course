class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.num_questions = len(question_list)
        self.current_question = question_list[0]
        self.current_question_index = 0
        self.correct_answers = 0

    def next_question(self):
        self.current_question = self.get_current_question()
        self.current_question_index += 1
        return input(f"Q.{self.current_question_index}: {self.current_question.question} (True/False)?").lower()

    def get_current_question(self):
        return self.question_list[self.current_question_index]

    def check_answer(self, user_answer):
        if user_answer == self.current_question.answer.lower():
            print("You got it!")
            self.correct_answers += 1
        else:
            print(f"Sorry, that's wrong. Correct answer was {self.current_question.answer}.")

        print(f"Your current score is {self.correct_answers}/{self.current_question_index}")

    def still_has_questions(self):
        return self.current_question_index < self.num_questions

    def print_summary(self):
        print(f"Thank you for playing! Your result {self.correct_answers} / {self.num_questions} questions.")

    # def game(self):
    #     print("Welcome to Quiz Game!")
    #     print(f"You have {self.num_questions} questions.")
    #     while self.current_question_index < self.num_questions:
    #         user_answer = self.next_question()
    #         self.check_answer(user_answer)
    #         self.current_question_index += 1

        #





