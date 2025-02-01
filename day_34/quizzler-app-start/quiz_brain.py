import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_question(self):

        if not self.still_has_questions():
            return
        self.current_question = self.question_list[self.question_number]
        return html.unescape(self.current_question.text)

    def next_question(self):
        self.question_number += 1
        return self.get_question()


    def check_answer(self, user_answer: bool):
        correct_answer = self.current_question.answer
        if str(user_answer) == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

        return self.score


    def game_over(self):
        print("game over")
