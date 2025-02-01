THEME_COLOR = "#375362"

import data as dt
import tkinter as tk


class QuizUI:
    def __init__(self, quiz_brain):
        # QuizBrain class object
        self.quiz = quiz_brain
        # Create the main application window
        self.window = tk.Tk()
        self.window.title("Quiz App")
        # 9:16 ratio example: 450x800, 360x640, etc.
        self.window.geometry("450x800")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Create a frame to hold the label and the numeric value
        score_frame = tk.Frame(self.window, bg=THEME_COLOR)
        score_frame.pack(side="top", anchor="ne")

        # Label for the text "Score:"
        self.score_label = tk.Label(
            score_frame,
            text="Score:",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 16, "bold")
        )
        self.score_label.pack(side="left", padx=(0, 5))

        # Label for the numeric value of the score
        self.score_value = tk.Label(
            score_frame,
            text="0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 16, "bold")
        )
        self.score_value.pack(side="left")

        # Question canvas in the middle
        self.canvas = tk.Canvas(
            self.window,
            width=300,  # canvas width
            height=400,  # canvas height
            bg="white",
            highlightthickness=0
        )
        self.question_text = self.canvas.create_text(
            150,  # x-position (center of canvas width)
            200,  # y-position (center of canvas height)
            text=self.quiz.get_question(),
            fill="black",
            font=("Arial", 20, "italic"),
            width=280  # wrap text at 280px
        )
        self.canvas.pack(pady=20)

        # self.display_question()

        # Load your images (check and X)
        self.true_image = tk.PhotoImage(file="./images/true.png")
        self.false_image = tk.PhotoImage(file="./images/false.png")

        # True (Check) button
        self.true_button = tk.Button(
            self.window,
            image=self.true_image,
            highlightthickness=0,
            command=self.press_true
        )
        # Keep a reference to avoid image getting garbage-collected
        self.true_button.image = self.true_image
        self.true_button.pack(side="left", expand=True)

        # False (X) button
        self.false_button = tk.Button(
            self.window,
            image=self.false_image,
            highlightthickness=0,
            command=self.press_false
        )
        self.false_button.image = self.false_image
        self.false_button.pack(side="right", expand=True)

        # self.window.mainloop()

    def display_question(self, q_txt):
        # get question from data.py question_data
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=q_txt)
        else:
            self.canvas.itemconfig(self.question_text, text=self.quiz.game_over())

    def press_true(self):
        """
        Handle the 'True' button being pressed.
        """
        if self.quiz.still_has_questions():
            print("True pressed")
            score = self.quiz.check_answer(True)
            self.update_score(score)
            question = self.quiz.next_question()
            self.display_question(question)
        else:
            print("play again")
            self.quiz.play_again()

    def press_false(self):
        """
        Handle the 'False' button being pressed.
        """
        if self.quiz.still_has_questions():
            print("False pressed")
            score = self.quiz.check_answer(False)
            self.update_score(score)
            question = self.quiz.next_question()
            self.display_question(question)
        else:
            print("exit")
            self.quiz.end_game()

    def update_score(self, new_score):
        self.score_value.config(text=str(new_score))


if __name__ == "__main__":
    QuizUI()
