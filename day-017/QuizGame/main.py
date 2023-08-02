# Day: 17
# Date: 02-Aug-2023
# Name: Quiz Game (using OOP)

# Quiz Object
# Attrib: q_text, q_answer

from data import question_data
from question_model import Question
from quiz_brain import QuestionBank
import os

# Import the questions from data.py and make them as Question objects

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_main = QuestionBank(question_bank)

os.system("clear")
while quiz_main.still_have_question():
    quiz_main.next_question()

print("You completed the quiz!")
print(f"Your final score: {quiz_main.score}/{quiz_main.question_number}")