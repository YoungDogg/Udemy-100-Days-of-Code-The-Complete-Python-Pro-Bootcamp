import random
from turtle import Screen
from day_19.turtle_race.day_19_turtle_race import TurtleGroup


class TurtleGame:
    def __init__(self, screen_x: int = 500, screen_y: int = 400):
        self.screen = Screen()
        self.screen.screensize(canvwidth=screen_x, canvheight=screen_y)
        self.turtle_group = TurtleGroup(screen=self.screen)
        self.is_game_over: bool = False
        self.winner_input: int = None
        self.winner_output: int = None

    def start_game(self):
        # require input exception error handling
        try:
            self.winner_input: int = (
                self.screen.numinput(title="Guess Winner", prompt="Number of the tutle:",
                                     minval=1, maxval=len(self.turtle_group.turtle_objects)))
            print(f"guessing tutle number: {int(self.winner_input)}")
        except TypeError:
            print("Input was cancelled or invalid. Defaulting to turtle number 0")
            self.winner_input = 0

        y_pos = -300
        num = 1
        for turtle in self.turtle_group.turtle_objects:
            turtle.teleport_turtle(x=-400, y=y_pos)
            turtle.write(arg=num, align="right", font=('arial', 20, 'bold'))
            y_pos += 120
            num += 1

    def run_turtle(self):
        """
        1. run until is_game_over True
        2. if any turtle reach to the right of the screen, game over
        3. all turtles move one time with same speed, different distance
        """
        while not self.is_game_over:
            for index, turtle in enumerate(self.turtle_group.turtle_objects):
                if turtle.position()[0] >= 490:  # 2.
                    self.is_game_over = True
                    # get turtle number
                    print(f"winner: {turtle}, index: {index}")
                    self.winner_output = index + 1
                    break
                rand_dist = random.randint(1, 60)
                turtle.goto(x=turtle.position()[0] + rand_dist, y=turtle.position()[1])

    def end_game(self):
        print(f"winner: turtle {self.winner_output}!!!!")
        if self.winner_input == self.winner_output:
            print("you won!")
        else:
            print("you lost")
