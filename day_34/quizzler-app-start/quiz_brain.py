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
        self.current_question = self.question_list[self.question_number]
        return html.unescape(self.current_question.text)

    def next_question(self):
        # self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # q_text = html.unescape(self.current_question.text)
        """
        This line diplays the question. UI can be here.
        But the join UI and this class should be at main.py not here.
        So, how to change it?
        To combine UI and this class, get q_text from here. And put it from main.py.
        """

        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer: bool):
        correct_answer = self.current_question.answer
        if user_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
