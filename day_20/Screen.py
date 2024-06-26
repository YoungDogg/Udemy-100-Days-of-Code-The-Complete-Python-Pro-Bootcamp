from turtle import Screen


class GameScreen:
    def __init__(self, width: int = 600, height: int = 400, tracer: int = 5):
        self.screen = Screen()
        self.screen.setup(width=width, height=height)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        # self.screen.tracer(tracer)
