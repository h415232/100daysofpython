#TODO: asking question
#TODO: checking if answer is correct
#TODO: checking if we're at the end of the quiz

# QuizBrain Class
# Attrib: question_number = 0, question_list, score
# Method: next_question -> to show the new question

class QuestionBank:

    def __init__(self, question_list:list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, answer):
        cur_question = self.question_list[self.question_number]
        correct_answer = cur_question.answer
        
        if correct_answer.lower() == answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print("That is wrong!")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print()
        print()


    def next_question(self):
        cur_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {cur_question.text} (True/False)?: ")

        self.check_answer(answer)
        self.question_number += 1

    def still_have_question(self):
        return self.question_number < len(self.question_list)

