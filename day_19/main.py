from turtle import Screen
from turtle_19 import Day19SketchTurtle


class TurtleApp:
    def __init__(self):
        self.trt = Day19SketchTurtle()
        self.scn = Screen()
        self.setup_screen()

    def setup_screen(self) -> None:
        self.scn.listen()
        self.scn.onkey(key="w", fun=self.trt.move_forward)
        self.scn.onkey(key="s", fun=self.trt.move_backward)
        self.scn.onkey(key="a", fun=self.trt.rotate_anti_clock)
        self.scn.onkey(key="d", fun=self.trt.rotate_clock)
        self.scn.onkey(key="c", fun=self.reset_screen)

    def reset_screen(self) -> None:
        self.scn.reset()

    def run(self) -> None:
        self.scn.mainloop()


if __name__ == "__main__":
    app = TurtleApp()
    app.run()
