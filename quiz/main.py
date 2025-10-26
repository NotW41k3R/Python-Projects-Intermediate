from data import question_data
from question_model import Question
from quiz_brain import AskQuestion

question_bank= []
for question in question_data:
    ques = Question(question["text"], question["answer"])
    question_bank.append(ques)

quiz = AskQuestion(question_bank)

quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz!")
print(f"Final Score {quiz.score}/{quiz.question_number}")
