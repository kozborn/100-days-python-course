from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from ui import QuizInterface
import html

question_bank = []
for question in question_data:
    question_category = html.unescape(question['category'])
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer, question_category)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quizUI = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quizUI.update_question(question)
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")


