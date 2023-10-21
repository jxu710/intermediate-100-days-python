from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    data = Question(item["text"], item["answer"])
    question_bank.append(data)

quiz = QuizBrain(question_bank)
quiz.next_question()

