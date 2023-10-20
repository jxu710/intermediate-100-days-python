from question_model import  Question
from data import question_data

question_bank = []

for item in question_data:
    data = Question(item["text"], item["answer"])
    question_bank.append(data)

print(question_bank[0].text)

