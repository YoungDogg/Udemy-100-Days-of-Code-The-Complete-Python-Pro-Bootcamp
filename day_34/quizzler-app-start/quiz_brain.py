import html
import sys
from question_model import Question
from data import QuestionData

class QuizBrain:

    def __init__(self):
        self.question_data = QuestionData()
        print(self.question_data.question_set_index)
        self.question_number = 0
        self.score = 0
        self.question_list = self.get_q_list()
        self.current_question = None

    def get_q_list(self):
        return [Question(q["question"],q["correct_answer"]) for q in self.question_data.fetch_new_questions()]

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
        print("**Game over**")
        return (f"**Game over**\n"
                f"Score: {self.score}\n"
                f"V for play again.\n"
                f"X for exit.")

    def play_again(self):
        """
        Restart the current program
        Reset question number
        Reset score
        Reset question
        """
        self.question_number = 0
        self.score = 0
        self.question_list = self.get_q_list()




    def end_game(self):
        sys.exit()