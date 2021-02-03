from question_model import Question
from  data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question())

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_ques():
    quizBrain.next_question()

print("You have Completed Your Quiz")
print(f"Your Score is {quizBrain.score}/{quizBrain.question_number}")
