from turtle import Screen


class GameScreen:
    def __init__(self, width: int = 600, height: int = 400, tracer: int = 0):
        self.screen = Screen()
        self.screen.setup(width=width, height=height)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        # TODO: uncomment this tracer
        self.screen.tracer(tracer)

    def update(self):
        self.screen.update()

    def listen(self):
        self.screen.listen()