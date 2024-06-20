from day_19.turtle_race.day_19_turtle_race import TurtleGroup


class TurtleGame:
    def __init__(self, screen_x: int = 500, screen_y: int = 400):
        self.turtle_group = TurtleGroup()
        self.screen = self.turtle_group.scn
        self.screen.screensize(canvwidth=screen_x, canvheight=screen_y)

    def start_game(self):
        # require input exception error handling
        winner_input: int = self.screen.numinput(title="Guess Winner", prompt="Number of the tutle:")
        print(f"guessing tutle number: {int(winner_input)}")

        y_pos = -300
        for turtle in self.turtle_group.turtle_objects:
            turtle.teleport_turtle(x=-400, y=y_pos)
            y_pos += 120
            # how to put numbers before turtles?

    def run_turtle(self):
        pass

    def end_game(self):
        pass
