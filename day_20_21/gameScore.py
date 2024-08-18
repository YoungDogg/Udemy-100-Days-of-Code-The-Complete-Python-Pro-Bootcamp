from turtle import Turtle


class GameScore:
    def __init__(self, snake, screen):
        self.snake = snake
        self.score_letter = Turtle()
        self.score_number = Turtle()
        self.score = self.snake.append_score()

        with open('highest_score.txt','r') as score_file:
            self.highest_score = score_file.read()
        print(f"self.highest_score: {self.highest_score}")
        self.highest_letter = Turtle()
        self.highest_number = Turtle()

        self.screen = screen
        self.screen_width = self.screen.window_width() / 2
        self.screen_height = self.screen.window_height() / 2

        self.text_pos = (self.screen_width * (1 - .4), self.screen_height * (1 - .2))
        self.number_pos = (self.screen_width * (1 - .2), self.screen_height * (1 - .2))
        self.highest_text_pos = (self.screen_width * (1 - .65), self.screen_height * (1 - .4))
        self.highest_number_pos = (self.screen_width * (1 - .2), self.screen_height * (1 - .405))

        self.font = ('Arial', 14, 'bold')

        self.displayLetter()
        self.displayScoreNumber()
        self.displayHighestLetter()
        self.displayHighestNumber()

    @staticmethod
    def display(obj, pos, content, font):
        obj.hideturtle()
        obj.color("white")
        obj.penup()
        obj.setpos(pos)
        obj.clear()
        obj.write(content, False, "left", font=font)

    def displayLetter(self):
        self.display(obj=self.score_letter, pos=self.text_pos, content="score: ", font=self.font)

    def displayScoreNumber(self):
        self.score = self.snake.append_score()
        self.display(obj=self.score_number, pos=self.number_pos, content=f"{self.score}", font=self.font)

    def displayHighestLetter(self):
        self.display(obj=self.highest_letter, pos=self.highest_text_pos, content="highest score: ", font=self.font)

    def displayHighestNumber(self):
        self.display(obj=self.highest_number, pos=self.highest_number_pos, content=f"{self.highest_score}", font=self.font)

    def updateHighestScore(self):
        if self.score > int(self.highest_score):
            with open('highest_score.txt','w') as score_file:
                score_file.write(str(self.score))
            with open('highest_score.txt','r') as score_file:
                self.highest_score = score_file.read()
