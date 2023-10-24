from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []

for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = html.unescape(question["correct_answer"])
    data = Question(question_text, question_answer)
    question_bank.append(data)

quiz = QuizBrain(question_bank)


while quiz.still_has_question() == True:
    quiz.next_question()


print("You completed the quiz")
print(f"your final score is {quiz.score} / {quiz.question_number}")

