import random
from data import question_data, mythology_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for q in mythology_data:
    question_bank.append(Question(question=q["question"], answer=q["answer"]))

random.shuffle(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()
    quiz.check_answer(answer)


