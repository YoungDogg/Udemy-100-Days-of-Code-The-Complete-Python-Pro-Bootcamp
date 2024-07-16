from turtle import Turtle


def display(obj, pos, content, font):
    obj.hideturtle()
    obj.color("white")
    obj.penup()
    obj.setpos(pos)
    obj.clear()
    obj.write(content, False, "left", font=font)


class GameScore:
    def __init__(self, snake, screen):
        self.snake = snake
        self.score_letter = Turtle()
        self.score_number = Turtle()

        self.screen = screen
        self.screen_width = self.screen.window_width() / 2
        self.screen_height = self.screen.window_height() / 2

        self.text_pos = (self.screen_width * (1 - .4), self.screen_height * (1 - .2))
        self.number_pos = (self.screen_width * (1 - .2), self.screen_height * (1 - .2))

        self.font = ('Arial', 14, 'bold')

        self.displayLetter()

    def displayLetter(self):
        display(obj=self.score_letter, pos=self.text_pos, content="score: ", font=self.font)

    def displayScoreNumber(self):
        score = self.snake.append_score()
        display(obj=self.score_number, pos=self.number_pos, content=f"{score}", font=self.font)
