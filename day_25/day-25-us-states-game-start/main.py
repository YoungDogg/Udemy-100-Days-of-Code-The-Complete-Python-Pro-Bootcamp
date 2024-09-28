import turtle
import tkinter
import time
from score import Score
from state_locator import StateLocator

# how to update score?
SCORE = 0


def main():
    # Make UI: the screen, pop-up window
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = Score(screen)
    data.display_ui_all()
    stateLocator = StateLocator(screen, data)

    turtle.Screen().onclick(stateLocator.return_coordinates)

    screen.mainloop()


if __name__ == "__main__":
    main()
