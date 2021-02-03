from data import question_data
import random

class Question:
    ALREADY_QUES = []
    def __init__(self):
        if(len(self.ALREADY_QUES) == len(question_data)):
            self.finished = True
        else:
            randQues = random.randint(0, len(question_data) - 1)
            while randQues in self.ALREADY_QUES:
                randQues = random.randint(0, len(question_data) - 1)
            ques = question_data[randQues]
            self.ALREADY_QUES.append(randQues)
            self.text = ques["text"]
            self.answer = ques["answer"]
            self.finished = False
