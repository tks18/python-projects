class QuizBrain:

    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def still_has_ques(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_num = self.question_number
        ques = self.question_list[q_num]
        self.question_number += 1
        u_answer = input(f"Q.{q_num + 1} {ques.text} ? (True / False) ").lower()
        self.check_answer(u_answer, ques.answer)

    def check_answer(self, u_answer, quest_answer):
        if u_answer == quest_answer.lower():
            print("Your Answer is Correct")
            self.score += 1
        else:
            print("Your Answer is Wrong")
        print(f"The Correct Answer is {quest_answer}")
        print(f"Your Score is {self.score}/{self.question_number}\n\n\n")
