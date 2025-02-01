from quiz_brain import QuizBrain
from ui import QuizUI

"""
TODO: get question from UI. scoring from UI
"""


class Main:


    quiz = QuizBrain()

    ui = QuizUI(quiz)

    # while quiz.still_has_questions():
    #     question_line = quiz.get_question()
    #     ui.display_question(question_line)
    #     quiz.next_question()

    # print("You've completed the quiz")
    # print(f"Your final score was: {quiz.score}/{quiz.question_number}")

    ui.window.mainloop()


if __name__ == "__main__":
    Main()
