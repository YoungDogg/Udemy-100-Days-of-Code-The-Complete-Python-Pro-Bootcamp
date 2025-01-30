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

        # Score label (top-right)
        self.score_label = tk.Label(
            self.window,
            text="score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 16, "bold")
        )
        self.score_label.pack(side="top", anchor="ne")

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
            text="Questions will be here.",
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

        self.canvas.itemconfig(self.question_text, text=q_txt)

    def press_true(self):
        """
        Handle the 'True' button being pressed.
        """
        print("True pressed")

    def press_false(self):
        """
        Handle the 'False' button being pressed.
        """
        print("False pressed")



if __name__ == "__main__":
    QuizUI()
