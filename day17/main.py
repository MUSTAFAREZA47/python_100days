from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    question_object = Question(q_text, q_answer)

    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# print(question_bank)