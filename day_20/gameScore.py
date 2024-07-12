from turtle import Turtle


class GameScore:
    score = 0
    def __init__(self, snake, screen):
        self.snake = snake
        self.screen = screen
        self.font = ('Arial', 12, 'bold')
        self.set_GUI()

    def set_GUI(self):
        screen_width = self.screen.window_width() / 2
        screen_height = self.screen.window_height() / 2
        text_pos = (screen_width * (1 - .4), screen_height * (1 - .2))
        score_board = Turtle()
        score_board.hideturtle()
        score_board.color("white")
        score_board.penup()
        score_board.setpos(text_pos)
        score_board.write("score: ", False, "left", font=self.font)

    @staticmethod
    def count_score(self):
        # every additional segment of snake will be counted as one
        score += 1
        pass

    pass
