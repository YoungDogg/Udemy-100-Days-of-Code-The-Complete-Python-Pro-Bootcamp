from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

"""
TODO: get question from UI. scoring from UI
"""


# class Main:
#     question_bank = []
#     for question in question_data:
#         question_text = question["question"]
#         question_answer = question["correct_answer"]
#         new_question = Question(question_text, question_answer)
#         question_bank.append(new_question)
#
#     quiz = QuizBrain(question_bank)
#
#     ui = QuizUI(quiz)
#
#     while quiz.still_has_questions():
#         question_line = quiz.get_question()
#         ui.display_question(question_line)
#         quiz.next_question()
#
#     print("You've completed the quiz")
#     print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    ui = QuizUI(quiz)

    while quiz.still_has_questions():
        question_line = quiz.get_question()
        ui.display_question(question_line)
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

    ui.window.mainloop()
