from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    data = Question(item["text"], item["answer"])
    question_bank.append(data)

quiz = QuizBrain(question_bank)


while quiz.still_has_question() == True:
    quiz.next_question()

if quiz.still_has_question() == False:
    print("You completed the quiz")
    print(f"your final score is {quiz.score}")

